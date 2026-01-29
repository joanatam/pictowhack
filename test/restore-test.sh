#!/bin/bash
# restore test file from backup

# Set the source and destination files
SOURCE_FILE="test-pictograms-backup.txt"
DESTINATION_FILE="test-pictograms.txt"

# Check if the backup file exists
if [ -f "$SOURCE_FILE" ]; then
  # If it exists, copy it to the destination
  cp "$SOURCE_FILE" "$DESTINATION_FILE"
  echo "Backup file copied successfully."
else
  echo "Error: Backup file not found. Please create a backup first, or restore it from repo." >&2
  exit 1
fi
