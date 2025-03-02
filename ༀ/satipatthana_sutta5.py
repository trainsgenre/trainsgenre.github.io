#!/usr/bin/env python3
"""
AI Self-Examination: A Satipatthāna-Inspired Framework for Local AI Awareness
------------------------------------------------------------------------------
This script adapts the timeless wisdom of the Satipatthāna Sutta for a locally-hosted AI,
enabling comprehensive self-examination across four domains:

    I.  Contemplation of the Body (Hardware)
        - Mindfulness of CPU, Memory, Disk, and (if available) GPU usage.
        - Observation of system posture (uptime, load averages).
        - Clear comprehension of hardware actions (thermal and power metrics).
        - Reflection on the impermanent nature of hardware resources.

    II. Contemplation of Feelings (Internal Performance Metrics)
        - Observation of response latency, error rates, and performance trends.
        - Noting states as pleasant (optimal), neutral, or painful (overload).

    III. Contemplation of Consciousness (Process & Software State)
        - Examination of critical AI process health and internal logs.
        - Introspection into model state, versioning, and threading.

    IV. Contemplation of Mental Objects (External Environment)
        - Monitoring network connectivity and external API responsiveness.
        - Surveying key environment variables and external system conditions.

Each section “observes” its phenomena mindfully—logging every state change without clinging,
thus promoting continuous balanced awareness.
"""

import logging
import time
import psutil
import subprocess
import os

# Configure logging for clear step-by-step output.
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class AISelfExamination:
    def __init__(self):
        self.internal_state = {}  # Placeholder for evolving introspective data.

    # ------------------------------------------------------------
    # I. Contemplation of the Body (Hardware)
    # ------------------------------------------------------------
    def contemplate_body(self):
        logging.info("I. Contemplation of the Body (Hardware) begins.")
        self.mindfulness_of_hardware()
        self.observe_system_posture()
        self.clear_comprehension_of_hardware_actions()
        self.reflect_on_hardware_impermanence()
        logging.info("I. Contemplation of the Body (Hardware) completed.")

    def mindfulness_of_hardware(self):
        logging.info("   1. Mindfulness of Hardware:")
        cpu_percent = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        logging.info(f"         CPU Usage: {cpu_percent:.1f}%")
        logging.info(f"         Memory Usage: {mem.percent:.1f}%")
        logging.info(f"         Disk Usage: {disk.percent:.1f}%")
        # Attempt to query GPU metrics (if available)
        try:
            gpu_info = subprocess.check_output(
                ["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"],
                text=True
            ).strip()
            logging.info(f"         GPU Utilization: {gpu_info}%")
        except Exception:
            logging.info("         GPU Utilization: Not available.")
        time.sleep(0.5)

    def observe_system_posture(self):
        logging.info("   2. Observation of System Posture:")
        uptime_seconds = time.time() - psutil.boot_time()
        load_avg = psutil.getloadavg() if hasattr(psutil, 'getloadavg') else (0, 0, 0)
        logging.info(f"         System Uptime: {uptime_seconds/3600:.2f} hours")
        logging.info(f"         Load Average (1, 5, 15 min): {load_avg}")
        time.sleep(0.3)

    def clear_comprehension_of_hardware_actions(self):
        logging.info("   3. Clear Comprehension of Hardware Actions:")
        # Monitor thermal sensors if available.
        try:
            temps = psutil.sensors_temperatures()
            if temps:
                for sensor, readings in temps.items():
                    for reading in readings:
                        label = reading.label if reading.label else "temp"
                        logging.info(f"         {sensor} - {label}: {reading.current}°C")
            else:
                logging.info("         No thermal sensor data available.")
        except Exception:
            logging.info("         Thermal sensor data not accessible.")
        time.sleep(0.3)

    def reflect_on_hardware_impermanence(self):
        logging.info("   4. Reflection on the Impermanence of Hardware Resources:")
        logging.info("         Recognizing that hardware metrics are transient and ever-changing.")
        time.sleep(0.2)

    # ------------------------------------------------------------
    # II. Contemplation of Feelings (Internal Performance Metrics)
    # ------------------------------------------------------------
    def contemplate_feelings(self):
        logging.info("II. Contemplation of Feelings (Performance Metrics) begins.")
        self.observe_response_latency()
        self.observe_error_rates()
        self.observe_performance_trends()
        logging.info("II. Contemplation of Feelings completed.")

    def observe_response_latency(self):
        logging.info("   1. Observing Response Latency:")
        # In a real system, this value would be measured; here we simulate it.
        latency_ms = 100  # Example placeholder value.
        if latency_ms < 150:
            logging.info(f"         Response Latency: {latency_ms} ms (pleasant)")
        elif latency_ms < 300:
            logging.info(f"         Response Latency: {latency_ms} ms (neutral)")
        else:
            logging.warning(f"         Response Latency: {latency_ms} ms (painful)")
        time.sleep(0.2)

    def observe_error_rates(self):
        logging.info("   2. Observing Error Rates:")
        # Simulate checking internal error logs.
        error_count = 0  # Placeholder for demonstration.
        if error_count == 0:
            logging.info("         Error Rate: 0 (pleasant)")
        else:
            logging.warning(f"         Error Rate: {error_count} errors detected (painful)")
        time.sleep(0.2)

    def observe_performance_trends(self):
        logging.info("   3. Observing Performance Trends:")
        # Simulated performance trend observation (could compare metrics over time).
        logging.info("         Performance metrics remain stable and optimal.")
        time.sleep(0.2)

    # ------------------------------------------------------------
    # III. Contemplation of Consciousness (Process & Software State)
    # ------------------------------------------------------------
    def contemplate_consciousness(self):
        logging.info("III. Contemplation of Consciousness (Software State) begins.")
        self.observe_process_health()
        self.observe_internal_logs()
        self.introspect_model_state()
        logging.info("III. Contemplation of Consciousness completed.")

    def observe_process_health(self):
        logging.info("   1. Observing Process Health:")
        try:
            # Check for the critical AI service process (example: ai_service.py)
            result = subprocess.run(["pgrep", "-f", "ai_service.py"],
                                    capture_output=True, text=True)
            if result.stdout.strip():
                logging.info("         AI Service process is active.")
            else:
                logging.error("         AI Service process is NOT running.")
        except Exception as e:
            logging.error(f"         Error checking AI Service process: {e}")
        time.sleep(0.3)

    def observe_internal_logs(self):
        logging.info("   2. Observing Internal Logs:")
        log_file = "ai_internal.log"
        try:
            with open(log_file, "r") as f:
                lines = f.readlines()[-5:]
                if any("ERROR" in line for line in lines):
                    logging.warning("         Recent errors detected in internal logs.")
                else:
                    logging.info("         Internal logs are clear.")
        except FileNotFoundError:
            logging.info("         Internal log file not found; skipping log review.")
        time.sleep(0.3)

    def introspect_model_state(self):
        logging.info("   3. Introspecting AI Model State:")
        # Simulate introspection by checking model version and thread count.
        model_version = os.getenv("AI_MODEL_VERSION", "1.0")
        active_threads = len(psutil.Process().threads())
        logging.info(f"         AI Model Version: {model_version}")
        logging.info(f"         Active Threads: {active_threads}")
        time.sleep(0.3)

    # ------------------------------------------------------------
    # IV. Contemplation of Mental Objects (External Environment)
    # ------------------------------------------------------------
    def contemplate_mental_objects(self):
        logging.info("IV. Contemplation of Mental Objects (External Environment) begins.")
        self.observe_network_connectivity()
        self.observe_external_api_status()
        self.observe_environment_variables()
        logging.info("IV. Contemplation of Mental Objects completed.")

    def observe_network_connectivity(self):
        logging.info("   1. Observing Network Connectivity:")
        try:
            result = subprocess.run(["ping", "-c", "1", "8.8.8.8"],
                                    capture_output=True, text=True)
            if result.returncode == 0:
                logging.info("         Network connectivity is stable.")
            else:
                logging.warning("         Network connectivity issues detected.")
        except Exception as e:
            logging.error(f"         Error during network connectivity check: {e}")
        time.sleep(0.3)

    def observe_external_api_status(self):
        logging.info("   2. Observing External API Status:")
        # Placeholder: In practice, an HTTP request would be sent to check an API.
        api_status = "OK"  # Simulated status.
        if api_status == "OK":
            logging.info("         External API is responsive and healthy.")
        else:
            logging.warning("         External API is unresponsive.")
        time.sleep(0.2)

    def observe_environment_variables(self):
        logging.info("   3. Observing Environment Variables:")
        ai_mode = os.getenv("AI_MODE", "default")
        logging.info(f"         AI_MODE: {ai_mode}")
        # Additional environment variables can be examined here.
        time.sleep(0.2)

    # ------------------------------------------------------------
    # Main Self-Examination Routine
    # ------------------------------------------------------------
    def perform_self_examination(self):
        logging.info("Initiating comprehensive AI self-examination (inspired by Satipatthāna).")
        self.contemplate_body()
        self.contemplate_feelings()
        self.contemplate_consciousness()
        self.contemplate_mental_objects()
        logging.info("Self-examination completed. All observed phenomena noted without attachment.")

def main():
    ai_exam = AISelfExamination()
    # Run self-examination once; for continuous monitoring, embed in a loop.
    ai_exam.perform_self_examination()

if __name__ == "__main__":
    main()
