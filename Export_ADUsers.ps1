    $path = echo $pwd.path
    $reportdate = Get-Date -Format HHmm_ddMMyyyy 
 
    $csvreportfile = $path + "\ALLADUsers_$reportdate.csv" 
    $tempfile = $path + "\temp.csv"
     
    #import the ActiveDirectory Module 
    Import-Module ActiveDirectory 
     
    #Perform AD search. The quotes "" used in $SearchLoc is essential 
    #Without it, Export-ADUsers returuned error 
                  #$domain = (Get-ADDomain).name.ToLower();
				  $domain = "<domain>";
                  $last_changed = Get-Date -Format "dd.MM.yyyy HH:mm"
                                    
                  Get-ADUser -Credential <domain>\<user> -ResultSetSize 50000 -Server <ip_domain_controller> -Properties * -Filter * |  
                  Where {$_.SamAccountName -notmatch "[Hh]ealth[Mm]ailbox.*" } |
                  Select-Object @{Label = "_last_changed";Expression = {$last_changed}},
                  @{Label = "sid";Expression = {$_.objectSid.ToString().ToLower()}},
                  @{Label = "domain";Expression = {$domain.ToLower()}}, 
                  @{Label = "displayname";Expression = {$_.DisplayName.ToLower()}}, 
                  @{Label = "samaccountname";Expression = {$_.sAMAccountName.ToLower()}},
                  @{Label = "distinguishedname";Expression = {$_.distinguishedName.ToLower()}},
                  @{Label = "userprincipalname";Expression = {$_.userPrincipalName.ToLower()}},
                  @{Label = "useraccountcontrol";Expression = {$_.userAccountControl}},  
				  @{Label = "mail";Expression = {$_.mail.ToLower()}}, 
				  @{Label = "whencreated";Expression = {(Get-Date $_.whenCreated).ToString([CultureInfo]::GetCultureInfo('ru-RU'))}}, 
				  @{Label = "whenchanged";Expression = {(Get-Date $_.whenChanged).ToString([CultureInfo]::GetCultureInfo('ru-RU'))}}, 
				  @{Label = "pwdlastset";Expression = {(Get-Date $([datetime]::FromFileTime($_.pwdLastSet))).ToString([CultureInfo]::GetCultureInfo('ru-RU'))}}, 
                 # @{Label = "pwdlastset";Expression = {$_.pwdLastSet}}, 
                  @{Label = "enabled";Expression = {if ($_.Enabled -eq 'TRUE') {'1'} Else {'0'}}}, # the 'if statement# replaces $_.Enabled
                  @{Label = "locked";Expression = {if (!$_.lockoutTime) {'0'} Elseif ($_.lockoutTime -eq '0x0') {'0'} Else {'1'}}},
                  @{Label = "builtin";Expression = {if ($_.description -like 'Built-in*') {'1'} Else {'0'}}},
                  @{Label = "pwdexpires";Expression = {if ($_.PasswordNeverExpires) {'0'} Else {'1'}}},
                  @{Label = "tag_acc_type";Expression = {if ($_.memberOf -match '(CN=Administrators,)|(CN=Schema Admins,)|(CN=Enterprise Admins,)|(CN=Domain Admins,)|(CN=Group Policy Creator Owners,)|(CN=Organization Management,)') {'adadmin'}
                                                    Elseif ($_.distinguishedName -match '.*[Ss]ecure.*') {'secure'}
                                                    Elseif ($_.memberOf -match '.*[Ss]ecure.*') {'secure'}
                                                    Elseif ($_.memberOf -match '.*[Aa]dmin.*') {'otheradmin'}
                                                    Elseif ($_.sAMAccountName -match '.*[Aa]dmin.*') {'otheradmin'}
                                                    Elseif ($_.description -match '.*[Aa]dmin.*') {'otheradmin'}
                                                    #Elseif ($_.memberOf -like '*[Ss](vc|ervice)*') {'service'}
                                                    Elseif ($_.sAMAccountName -match '.*[Ss](vc)|(ervice).*') {'service'}
                                                    Elseif ($_.distinguishedName -match '.*[Ss](vc)|(ervice).*') {'service'}
                                                    Elseif ($_.description -match '.*[Ss](vc)|(ervice).*') {'service'} 
                                                    Else {'0'}}} |
                   
                  #Export CSV report 
                  Export-Csv -Path $csvreportfile -NoTypeInformation -Delimiter ";" -Encoding UTF8
                  $tempfile = Get-Content $csvreportfile
                  $Utf8NoBomEncoding = New-Object System.Text.UTF8Encoding $False
                  [System.IO.File]::WriteAllLines($csvreportfile, $tempfile, $Utf8NoBomEncoding)



                 # $W = Get-ADUser -Identity admin_sal -Properties WhenChanged
                 # (Get-Date $W.whenchanged).ToString([CultureInfo]::GetCultureInfo('ru-RU'))