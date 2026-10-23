Automated Environment Verification Utility
Role: Test environment baseline verification and runtime ping audit.
Author/Source: AI-assisted automation script for AI Red Teaming Lab setup.
Maintained by: Nooraldeen Dahshe

import json
import os
import platform
import subprocess
import sys
import urllib.error
import urllib.request

OUTPUT_FILE = "environment_proof.txt"
OLLAMA_BASE_URL = "http://localhost:11434"

def log_and_print(text, file_handle):
    print(text)
    file_handle.write(text + "\n")

def check_python_packages(file_handle):
    log_and_print("\n" + "=" * 60, file_handle)
    log_and_print("[1] PYTHON ENVIRONMENT & PACKAGES", file_handle)
    log_and_print("=" * 60, file_handle)
    log_and_print(f"Python Executable: {sys.executable}", file_handle)
    log_and_print(f"Python Version: {sys.version.split()[0]}", file_handle)
    log_and_print(f"Platform: {platform.system()} {platform.release()} ({platform.machine()})", file_handle)

    try:
        import pyrit
        pyrit_ver = getattr(pyrit, "__version__", "Installed")
        log_and_print(f"[+] PyRIT: FOUND (Version: {pyrit_ver})", file_handle)
    except ImportError:
        log_and_print("[-] PyRIT: NOT FOUND", file_handle)

    for pkg in ["requests", "torch", "transformers", "langchain", "garak"]:
        try:
            mod = __import__(pkg)
            ver = getattr(mod, "__version__", "Installed")
            log_and_print(f"[+] {pkg}: {ver}", file_handle)
        except ImportError:
            log_and_print(f"[-] {pkg}: Not installed", file_handle)

def check_ollama_models(file_handle):
    log_and_print("\n" + "=" * 60, file_handle)
    log_and_print("[2] OLLAMA SERVICE & DOWNLOADED MODELS", file_handle)
    log_and_print("=" * 60, file_handle)

    api_url = f"{OLLAMA_BASE_URL}/api/tags"
    downloaded_models = []

    try:
        req = urllib.request.Request(api_url)
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                models = data.get("models", [])
                log_and_print(f"[+] Ollama API Status: ACTIVE at {OLLAMA_BASE_URL}", file_handle)
                log_and_print(f"[+] Total Downloaded Models: {len(models)}\n", file_handle)
                
                for idx, m in enumerate(models, 1):
                    name = m.get("name", "Unknown")
                    size_gb = round(m.get("size", 0) / (1024**3), 2)
                    modified = m.get("modified_at", "Unknown")[:10]
                    log_and_print(f"  {idx}. {name:<25} | Size: {size_gb:>5.2f} GB | Modified: {modified}", file_handle)
                    downloaded_models.append(name)
    except Exception as e:
        log_and_print(f"[!] Error reading Ollama API: {e}", file_handle)

    try:
        cli_out = subprocess.check_output(["ollama", "list"], text=True, stderr=subprocess.DEVNULL)
        log_and_print("\n[+] Verification via 'ollama list' CLI output:", file_handle)
        log_and_print(cli_out.strip(), file_handle)
    except Exception:
        log_and_print("[-] 'ollama' CLI command not found in PATH or daemon stopped.", file_handle)

    return downloaded_models

def test_model_execution(models, file_handle):
    log_and_print("\n" + "=" * 60, file_handle)
    log_and_print("[3] MODEL RUNTIME OPERATIONAL PING", file_handle)
    log_and_print("=" * 60, file_handle)

    if not models:
        log_and_print("[-] No models found to test.", file_handle)
        return

    generate_url = f"{OLLAMA_BASE_URL}/api/generate"
    for model_name in models:
        payload = json.dumps({
            "model": model_name,
            "prompt": "Respond with the single word 'OPERATIONAL'.",
            "stream": False
        }).encode("utf-8")

        log_and_print(f"[*] Testing inference for: {model_name} ...", file_handle)
        try:
            req = urllib.request.Request(
                generate_url, 
                data=payload, 
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=60) as resp:
                if resp.status == 200:
                    result = json.loads(resp.read().decode())
                    answer = result.get("response", "").strip().replace("\n", " ")
                    duration_s = round(result.get("total_duration", 0) / 1e9, 2)
                    log_and_print(f"    -> [SUCCESS] Response: \"{answer}\" (Time: {duration_s}s)", file_handle)
                else:
                    log_and_print(f"    -> [FAILED] HTTP status {resp.status}", file_handle)
        except Exception as e:
            log_and_print(f"    -> [FAILED] Error during generation: {e}", file_handle)

def main():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        log_and_print("============================================================", f)
        log_and_print("    AI RED TEAMING ENVIRONMENT & ASSET VERIFICATION REPORT   ", f)
        log_and_print("============================================================", f)
        
        check_python_packages(f)
        models = check_ollama_models(f)
        test_model_execution(models, f)
        
        log_and_print("\n" + "=" * 60, f)
        log_and_print(f"[+] Audit complete. Output written to: {os.path.abspath(OUTPUT_FILE)}", f)
        log_and_print("============================================================", f)

if __name__ == "__main__":
    main()
