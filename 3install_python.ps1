


Check_Program_Installed("python")

if (Check_Program_Installed = True ) { modules }
else { installer }



Check_Program_Installed("python")

if (Check_Program_Installed = True ) { modules }







function Check_Program_Installed( $programName ) {
    $wmi_check = (Get-WMIObject -Query "SELECT * FROM Win32_Product Where Name Like '%$programName%'").Length -gt 0
    return $wmi_check;
}
     




function installer() {
    mkdir C:\Users\$env:username\bin\python
    $url = "https://www.python.org/ftp/python/3.9.2/python-3.9.2.exe"
    $pat = "C:\Users\$env:username\bin\python"
    $client = new-object System.Net.WebClient
    $client.DownloadFile("$url", "$pat\python-3.9.2.exe")
    
    setx PYTHON_HOME "%USERPROFILE%\bin\python\python-3.7.0.exe” /quiet PrependPath=1
}






function modules {
    pip install scapy
    pip install 
    pip install
    pip install
    pip install
    pip install 
}
