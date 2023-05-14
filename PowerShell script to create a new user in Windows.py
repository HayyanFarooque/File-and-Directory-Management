$UserPassword = ConvertTo-SecureString -String "P@ssword" -AsPlainText -Force
$UserCredential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "NewUser", $UserPassword
New-LocalUser "NewUser" -Password $UserCredential.Password -FullName "New User" -Description "This is a new user."
