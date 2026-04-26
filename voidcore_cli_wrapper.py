#!/usr/bin/env python3
"""
VoidCore CLI Wrapper - Direct integration with Gemini CLI
Intercepts prompts and applies ultra-extreme compression before API calls.
"""

import sys
import os
import json
import argparse
from pathlib import Path
from typing import Optional, Dict
import subprocess

from voidcore_core import VoidCoreCompressor


class GeminiCLIWrapper:
    """Wrapper that intercepts Gemini CLI calls."""
    
    def __init__(self, config_path: Optional[str] = None):
        self.config = self._load_config(config_path)
        self.compressor = VoidCoreCompressor(config=self.config)
        self.verbose = self.config.get('verbose', False)
    
    def _load_config(self, config_path: Optional[str]) -> Dict:
        """Load configuration from JSON file."""
        default_config = {
            'verbose': False,
            'aggressive': True,
            'enable_textrank': True,
            'enable_delta': True,
            'enable_caveman': True,
            'enable_bpe': True,
            'enable_vowels': True,
            'enable_context': True,
            'enable_code_compression': True,
            'density_threshold': 0.2,
            'cache_file': '.voidcore_cache',
            'show_stats': True,
            'show_diff': False,
        }
        
        # Check for user config
        config_candidates = [
            config_path,
            Path.home() / '.voidcore' / 'config.json',
            Path('.voidcore.json'),
        ]
        
        for candidate in config_candidates:
            if candidate and Path(candidate).exists():
                try:
                    with open(candidate, 'r') as f:
                        user_config = json.load(f)
                        default_config.update(user_config)
                        if self.verbose:
                            print(f"✓ Loaded config from {candidate}")
                        break
                except Exception as e:
                    print(f"⚠ Failed to load config from {candidate}: {e}")
        
        return default_config
    
    def compress_prompt(self, prompt: str) -> Dict:
        """Compress a single prompt."""
        result = self.compressor.compress(
            prompt,
            aggressive=self.config.get('aggressive', True)
        )
        return result
    
    def print_stats(self, result: Dict):
        """Print compression statistics."""
        stats = result['stats']
        print("\n" + "="*60)
        print("🕳️  VOIDCORE COMPRESSION REPORT")
        print("="*60)
        print(f"📊 Original tokens:    {stats['original_tokens']:>5}")
        print(f"🗜️  Compressed tokens:  {stats['compressed_tokens']:>5}")
        print(f"💾 Token savings:      {stats['compression_ratio']:>5.1f}%")
        print(f"⚙️  Stages applied:    {', '.join(stats['stages_applied'])}")
        
        if self.config.get('show_diff', False):
            print("\n" + "-"*60)
            print("BEFORE:")
            print(result['original'][:200] + "..." if len(result['original']) > 200 else result['original'])
            print("\nAFTER:")
            print(result['compressed'][:200] + "..." if len(result['compressed']) > 200 else result['compressed'])
        
        print("="*60 + "\n")
    
    def run_gemini_with_compression(self, args: list) -> int:
        """
        Run Gemini CLI with prompt compression.
        
        Usage: voidcore-cli [options] -- [gemini-cli-args]
        """
        # Parse our options
        parser = argparse.ArgumentParser(description='VoidCore Gemini CLI Wrapper')
        parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
        parser.add_argument('--config', '-c', type=str, help='Config file path')
        parser.add_argument('--no-aggressive', action='store_true', help='Disable aggressive compression')
        parser.add_argument('--show-stats', action='store_true', help='Show compression stats')
        parser.add_argument('--show-diff', action='store_true', help='Show before/after diff')
        
        # Find -- separator
        try:
            sep_idx = args.index('--')
            voidcore_args = args[:sep_idx]
            gemini_args = args[sep_idx+1:]
        except ValueError:
            voidcore_args = []
            gemini_args = args
        
        # Parse voidcore args
        parsed = parser.parse_args(voidcore_args)
        self.verbose = parsed.verbose or self.config.get('verbose', False)
        
        if parsed.config:
            self.config = self._load_config(parsed.config)
        
        if parsed.no_aggressive:
            self.config['aggressive'] = False
        
        if parsed.show_stats:
            self.config['show_stats'] = True
        
        if parsed.show_diff:
            self.config['show_diff'] = True
        
        if self.verbose:
            print(f"🔧 VoidCore config: {json.dumps(self.config, indent=2)}")
            print(f"📝 Gemini args: {gemini_args}")
        
        # If prompt is passed as argument, compress it
        if gemini_args:
            # Try to find the prompt (usually last argument or after --prompt)
            prompt_idx = -1
            if '--prompt' in gemini_args:
                prompt_idx = gemini_args.index('--prompt') + 1
            elif '-p' in gemini_args:
                prompt_idx = gemini_args.index('-p') + 1
            
            if prompt_idx > 0 and prompt_idx < len(gemini_args):
                original_prompt = gemini_args[prompt_idx]
                result = self.compress_prompt(original_prompt)
                
                if self.config.get('show_stats', True):
                    self.print_stats(result)
                
                # Replace original prompt with compressed
                gemini_args[prompt_idx] = result['compressed']
        
        # Build and execute Gemini CLI command
        # Note: Assuming 'gemini' is the actual CLI command
        gemini_cmd = ['gemini'] + gemini_args
        
        if self.verbose:
            print(f"🚀 Executing: {' '.join(gemini_cmd)}")
        
        try:
            result = subprocess.run(gemini_cmd, cwd=os.getcwd())
            return result.returncode
        except FileNotFoundError:
            print("❌ Error: 'gemini' CLI not found in PATH")
            print("   Make sure Gemini CLI is installed and accessible")
            return 1
        except Exception as e:
            print(f"❌ Error running Gemini CLI: {e}")
            return 1


class InteractiveMode:
    """Interactive compression mode for testing."""
    
    def __init__(self):
        self.compressor = VoidCoreCompressor()
    
    def run(self):
        """Run interactive compression session."""
        print("\n" + "="*60)
        print("🕳️  VoidCore Interactive Compression Mode")
        print("="*60)
        print("Enter prompts to compress (type 'exit' to quit, 'help' for options)\n")
        
        while True:
            try:
                prompt = input("📝 Enter prompt: ")
                
                if prompt.lower() == 'exit':
                    print("\n👋 Goodbye!")
                    break
                
                if prompt.lower() == 'help':
                    self.print_help()
                    continue
                
                if not prompt.strip():
                    continue
                
                result = self.compressor.compress(prompt)
                
                print("\n" + "-"*60)
                print(f"✓ Original: {result['stats']['original_tokens']} tokens")
                print(f"✓ Compressed: {result['stats']['compressed_tokens']} tokens")
                print(f"✓ Savings: {result['stats']['compression_ratio']:.1f}%")
                print(f"✓ Stages: {', '.join(result['stats']['stages_applied'])}")
                print("\n📤 Compressed output:")
                print(f"   {result['compressed']}")
                print("-"*60 + "\n")
            
            except KeyboardInterrupt:
                print("\n\n👋 Interrupted!")
                break
            except Exception as e:
                print(f"❌ Error: {e}\n")
    
    def print_help(self):
        """Print help message."""
        help_text = """
Available commands:
  exit     - Exit interactive mode
  help     - Show this help message
  
Just type your prompt and press Enter to compress it.
        """
        print(help_text)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='VoidCore - Ultra-extreme token compression for Gemini CLI'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Interactive mode
    interactive_parser = subparsers.add_parser('interactive', help='Interactive compression mode')
    interactive_parser.add_argument('--config', '-c', type=str, help='Config file')
    
    # Compression command
    compress_parser = subparsers.add_parser('compress', help='Compress a single prompt')
    compress_parser.add_argument('prompt', nargs='?', help='Prompt to compress')
    compress_parser.add_argument('--config', '-c', type=str, help='Config file')
    compress_parser.add_argument('--aggressive', '-a', action='store_true', help='Use aggressive compression')
    compress_parser.add_argument('--show-diff', action='store_true', help='Show before/after')
    
    # Gemini integration
    gemini_parser = subparsers.add_parser('gemini', help='Run Gemini CLI with compression')
    gemini_parser.add_argument('gemini_args', nargs=argparse.REMAINDER, help='Gemini CLI arguments')
    gemini_parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    gemini_parser.add_argument('--config', '-c', type=str, help='Config file')
    
    # Parse arguments
    args = parser.parse_args()
    
    if not args.command:
        # Default to interactive mode
        print("No command specified. Starting interactive mode...")
        InteractiveMode().run()
        return 0
    
    if args.command == 'interactive':
        InteractiveMode().run()
        return 0
    
    elif args.command == 'compress':
        if not args.prompt:
            print("❌ Error: No prompt provided")
            print("   Usage: voidcore compress '<your prompt>'")
            return 1
        
        wrapper = GeminiCLIWrapper(config_path=args.config)
        result = wrapper.compress_prompt(args.prompt)
        
        print(f"\n📊 Original: {result['stats']['original_tokens']} tokens")
        print(f"🗜️  Compressed: {result['stats']['compressed_tokens']} tokens")
        print(f"💾 Savings: {result['stats']['compression_ratio']:.1f}%")
        
        if args.show_diff:
            print(f"\nBEFORE ({len(args.prompt)} chars):")
            print(args.prompt)
            print(f"\nAFTER ({len(result['compressed'])} chars):")
            print(result['compressed'])
        else:
            print(f"\nCompressed:")
            print(result['compressed'])
        
        return 0
    
    elif args.command == 'gemini':
        wrapper = GeminiCLIWrapper(config_path=args.config)
        if args.verbose:
            wrapper.verbose = True
        return wrapper.run_gemini_with_compression(args.gemini_args)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
