text = """
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException

2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException

2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException

2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException

2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
2023-06-30T19:05:48.984438439Z stdout F Progress (1): 2.7/5.9 kB
Progress (1): 5.5/5.9 kB
Progress (1): 5.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.0.0.M2a/org.eclipse.sisu.plexus-0.0.0.M2a.pom (5.9 kB at 1.3 kB/s)
2023-06-30T19:05:51.163536374Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom
2023-06-30T19:05:51.351864862Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.0.0.M2a/sisu-plexus-0.0.0.M2a.pom (7.9 kB at 44 kB/s)
2023-06-30T19:05:51.397998232Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom
2023-06-30T19:05:52.578748309Z stdout F Progress (1): 1.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.0/cdi-api-1.0.pom (1.4 kB at 1.2 kB/s)
2023-06-30T19:05:52.693523258Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom
2023-06-30T19:05:52.873582178Z stdout F Progress (1): 2.4 kB
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-parent/1.0/weld-api-parent-1.0.pom (2.4 kB at 17 kB/s)
2023-06-30T19:05:52.900459444Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom
2023-06-30T19:05:53.065045019Z stdout F Progress (1): 2.7/7.9 kB
Progress (1): 5.5/7.9 kB
Progress (1): 7.9 kB    
                    
Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-api-bom/1.0/weld-api-bom-1.0.pom (7.9 kB at 47 kB/s)
2023-06-30T19:05:53.151233202Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/6/weld-parent-6.pom
2023-06-30T19:05:53.569433518Z stdout P Progress (1): 2.7/21 kB
Progress (1): 5.5/21 kB
Progress (1): 8.2/21 kB
Progress (1): 11/21 kB 
Progress (1): 14/21 kB
Progress (1): 16/21 kB
Progress (1): 19/21 kB
Progress (1): 21 kB   
2023-06-30T19:13:40.253215858Z stdout F [INFO] Scanning for projects...
2023-06-30T19:18:10.102860417Z stdout F Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom
2023-06-30T19:27:53.641587359Z stdout F [ERROR] [ERROR] Some problems were encountered while processing the POMs:
2023-06-30T19:27:53.644675661Z stdout F [FATAL] Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10
2023-06-30T19:27:53.644694991Z stdout F  @ 
2023-06-30T19:28:50.377151659Z stdout F [ERROR] The build could not read 1 project -> [Help 1]
2023-06-30T19:28:50.401450098Z stdout F [ERROR]   
2023-06-30T19:28:50.430418122Z stdout F [ERROR]   The project com.practice:app:0.0.1-SNAPSHOT (/app/pom.xml) has 1 error
2023-06-30T19:28:50.432099912Z stdout F [ERROR]     Non-resolvable parent POM for com.practice:app:0.0.1-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:2.7.0 from/to central (https://repo.maven.apache.org/maven2): transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/2.7.0/spring-boot-starter-parent-2.7.0.pom and 'parent.relativePath' points at no local POM @ line 5, column 10: Remote host terminated the handshake: SSL peer shut down incorrectly -> [Help 2]
2023-06-30T19:28:50.437470917Z stdout F [ERROR] 
2023-06-30T19:29:04.020789927Z stdout F [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2023-06-30T19:29:04.02604921Z stdout F [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2023-06-30T19:29:04.026059731Z stdout F [ERROR] 
2023-06-30T19:29:04.026064418Z stdout F [ERROR] For more information about the errors and possible solutions, please read the following articles:
2023-06-30T19:29:04.026067809Z stdout F [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
2023-06-30T19:29:04.026070582Z stdout F [ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
"""


offset = 4096
print(text[:offset])
if len(text) > offset:
    for i in range(offset, len(text), offset):
        print(''.join(text[i:i + offset]))
