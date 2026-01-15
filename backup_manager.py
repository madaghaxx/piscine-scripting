import sys
import os
import subprocess
import signal
from datetime import datetime

#!/usr/bin/env python3


LOG_FILE = "./logs/backup_manager.log"
SCHEDULES_FILE = "backup_schedules.txt"
BACKUPS_DIR = "./backups"
SERVICE_SCRIPT = "backup_service.py"


def log_message(message):
    """Log a message with timestamp to the log file."""
    try:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        timestamp = datetime.now().strftime("[%d/%m/%Y %H:%M]")
        with open(LOG_FILE, "a") as log:
            log.write(f"{timestamp} {message}\n")
    except Exception as e:
        print(f"Error writing to log: {e}")


def get_service_pid():
    """Find the PID of the running backup_service.py process."""
    try:
        result = subprocess.run(
            ["ps", "-A", "-f"],
            capture_output=True,
            text=True
        )
        for line in result.stdout.split('\n'):
            if SERVICE_SCRIPT in line and 'python' in line.lower():
                parts = line.split()
                return int(parts[1])
        return None
    except Exception:
        return None


def start_service():
    """Start the backup service in the background."""
    try:
        if get_service_pid() is not None:
            log_message("Error: backup_service already running")
            return
        
        subprocess.Popen(
            ["python3", SERVICE_SCRIPT],
            start_new_session=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        log_message("backup_service started")
    except Exception:
        log_message("Error: can't start backup_service")


def stop_service():
    """Stop the backup service."""
    try:
        pid = get_service_pid()
        if pid is None:
            log_message("Error: backup_service not running")
            return
        
        os.kill(pid, signal.SIGTERM)
        log_message("backup_service stopped")
    except Exception:
        log_message("Error: can't stop backup_service")


def create_schedule(schedule):
    """Add a new backup schedule to the schedules file."""
    try:
        parts = schedule.split(';')
        if len(parts) != 3 or not parts[0] or not parts[1] or not parts[2]:
            log_message(f"Error: malformed schedule: {schedule}")
            return
        
        time_parts = parts[1].split(':')
        if len(time_parts) != 2:
            log_message(f"Error: malformed schedule: {schedule}")
            return
        
        try:
            hour = int(time_parts[0])
            minute = int(time_parts[1])
            if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                log_message(f"Error: malformed schedule: {schedule}")
                return
        except ValueError:
            log_message(f"Error: malformed schedule: {schedule}")
            return
        
        with open(SCHEDULES_FILE, "a") as f:
            f.write(f"{schedule}\n")
        
        log_message(f"New schedule added: {schedule}")
    except Exception:
        log_message(f"Error: malformed schedule: {schedule}")


def list_schedules():
    """List all backup schedules with index."""
    try:
        if not os.path.exists(SCHEDULES_FILE):
            log_message("Error: can't find backup_schedules.txt")
            return
        
        with open(SCHEDULES_FILE, "r") as f:
            schedules = f.readlines()
        
        for i, schedule in enumerate(schedules):
            print(f"{i}: {schedule.strip()}")
        
        log_message("Show schedules list")
    except Exception:
        log_message("Error: can't find backup_schedules.txt")


def delete_schedule(index_str):
    """Delete a schedule at the specified index."""
    try:
        if not os.path.exists(SCHEDULES_FILE):
            log_message("Error: can't find backup_schedules.txt")
            return
        
        index = int(index_str)
        
        with open(SCHEDULES_FILE, "r") as f:
            schedules = f.readlines()
        
        if index < 0 or index >= len(schedules):
            log_message(f"Error: can't find schedule at index {index}")
            return
        
        schedules.pop(index)
        
        with open(SCHEDULES_FILE, "w") as f:
            f.writelines(schedules)
        
        log_message(f"Schedule at index {index} deleted")
    except ValueError:
        log_message(f"Error: can't find schedule at index {index_str}")
    except Exception:
        log_message("Error: can't find backup_schedules.txt")


def list_backups():
    """List all backup files in the backups directory."""
    try:
        if not os.path.exists(BACKUPS_DIR):
            log_message("Error: can't find backups directory")
            return
        
        backups = os.listdir(BACKUPS_DIR)
        for backup in sorted(backups):
            print(backup)
        
        log_message("Show backups list")
    except Exception:
        log_message("Error: can't find backups directory")


def main():
    if len(sys.argv) < 2:
        print("Usage: backup_manager.py [start|stop|create|list|delete|backups]")
        return
    
    command = sys.argv[1]
    
    if command == "start":
        start_service()
    elif command == "stop":
        stop_service()
    elif command == "create":
        if len(sys.argv) < 3:
            print("Usage: backup_manager.py create [schedule]")
            return
        create_schedule(sys.argv[2])
    elif command == "list":
        list_schedules()
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: backup_manager.py delete [index]")
            return
        delete_schedule(sys.argv[2])
    elif command == "backups":
        list_backups()
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()