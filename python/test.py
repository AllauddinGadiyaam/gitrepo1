#!/usr/bin/env python3
import os
import datetime
import platform

print("=== Jenkins Python Demo Started ===")
print(f"Server: {platform.node()}")
print(f"OS: {platform.system()} {platform.release()}")
print(f"Time: {datetime.datetime.now()}")

# Write build info to file
with open("jenkins_build.txt", "w") as f:
    f.write(f"Build run at: {datetime.datetime.now()}\n")
    f.write(f"Hostname: {platform.node()}\n")
    f.write(f"Jenkins Workspace: {os.getcwd()}\n")

print("✅ Demo script completed successfully!")
print("=== Check jenkins_build.txt for details ===")
