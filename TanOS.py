import time
from tqdm import tqdm
from tqdm import tnrange,  tqdm_notebook
import os
from rich import print 
from rich.progress import track
from colorama import init, Fore, Back, Style

init()

print('Start TanOs')
time.sleep(3)
print('Loading...')
for i in track(range(3), description="Processing..."):
    time.sleep(1)  # Simulate work being done

time.sleep(2)
print('start disc (C:)')
for i in track(range(6), description="Processing..."):
    time.sleep(1)  # Simulate work being done
raml = '350mb'
roml = '643mb'
print('RAM1' + raml)
print('ROM1' + roml)
print('Type "help--" to ener list of commands')
time.sleep(3)
print('TanOs v9.0')
print('Tonibrozz corparation')
while True:
	command1 = input("C:/user/TanOs:")
	if command1 == "systeminfo":
		print('TanOs version v9.0 Uknown Copy')
	if command1 == "help--":
		print('systeminfo -- shows properties of your system\n ls -- shows all file\n echo -- print message\n Doom -- game Doom\n calc -- shows to Calculator\nexit -- exit system\nC:/ -- shows ram, cpu, rom\nRegedit -- shows setings for TanOs\nStore-- shows Store\nopen "Folder name" folder\nopen "program name\npaint -- shows paint -- open Paint\nopen D: -- shows disc D:\nwindows regedit -- shows windows regedit -- open windows regedit"')
	if command1 == 'open Recovery folder':
		print('File....:Recovery.dat')
	if command1 == 'open Rbtecovery.dat':
		print('file enoty')

	if command1 == "Doom":
		print('you not setup Doom')




	if command1 == 'Store--':
		print('wait....')
		time.sleep(3)
		print('installation check')
		time.sleep(5)
		print('Secend....')
		print('It is not windows this is TanOs v9.0')

	if command1 == 'exit':
		print('wait....')
		time.sleep(3)
		exit()

	if command1 == 'Regedit':
		print('Folder....:Tonibrozz')
		time.sleep(1)
		print('Folder....:TanOs4')
		time.sleep(1)
		print('Folder....:system42')

		command1 = input("C:RegEdit:")
	if command1 == 'open Tonibrozz folder':
		print('Folder....:0409')
		print('Folder....:AdvancedInstallers')
		print('Folder....:appmgmt')
		print('Folder....:CatRoot')
		print('Folder....:DRVSTORE')
		print('Folder....:en-US')
		print('Folder....:ru-RU')
		print('Folder....:TosBioPlugIns')

	if command1 == 'paint':
		os.system('C:/Windows/system32/mspaint.exe')
		
	if command1 == 'windows regedit':
		os.system('"C:/Windows/SysWOW64/regedit.exe"')

	if command1 == 'open 0409 folder':
		print('Folder....:0409')
		print('Folder....:AdvancedInstallers')
		print('Folder....:appmgmt')
		print('Folder....:CatRoot')
		print('Folder....:DRVSTORE')
		print('Folder....:en-US')
		print('Folder....:ru-RU')
		print('Folder....:TosBioPlugIns')


	if command1 == 'open AdvancedInstallers folder':
		print('Folder....:0409')
		print('Folder....:AdvancedInstallers')
		print('Folder....:appmgmt')
		print('Folder....:CatRoot')
		print('Folder....:DRVSTORE')
		print('Folder....:en-US')
		print('Folder....:ru-RU')
		print('Folder....:TosBioPlugIns')

	if command1 == 'open appmgmt folder':
		print('Folder....:0409')
		print('Folder....:AdvancedInstallers')
		print('Folder....:appmgmt')
		print('Folder....:CatRoot')
		print('Folder....:DRVSTORE')
		print('Folder....:en-US')
		print('Folder....:ru-RU')
		print('Folder....:TosBioPlugIns')

	if command1 == 'open CatRoot folder':
		print('File....:{127D0A1D-4EF2-11D1-8608-00C04FC295EE}.ini')
		print('File....:{F750E6C3-38EE-11D1-85E5-00C04FC295EE}.dll')
	if command1 == 'open TosBioPlugIns folder':
		print('File....:FaceRecognitionEngineAdapter.dll')
		print('File....:FaceRecognitionEngineAdapterResources.dll')
		print('File....:FaceRecognitionSensorAdapter.dll')
		print('File....:NUIVoiceWBSAdapters.dll')
		print('File....:en-US.txt')	

	if command1 == 'open DRVSTORE folder':
		print('file enpty')

	if command1 == 'open TanOs4 folder':
		print('Folder....:Recovery')

	if command1 == 'open Recovery folder':
		print('File....:Recovery.dat')

	if command1 == 'open Recovery.dat':
		print('file enoty')

	if command1 == 'open system42 folder':
		print('Foile....:apds.dll')
		print('Foile....:APHostClient.dll')
		print('Foile....:APHostRes.dll')
		print('Foile....:ApnDatabase.xml')
		print('Foile....:AppCapture.dll')
		print('Foile....:asferror.dll')
		print('Foile....:aspnet_counters.dll')
		print('proqram....:azman.msc')
		print('File....:blackbox12.dll')
		print('File....:C_43712.NLS')
		print('File....:C_114412.NLS')
		print('File....:apds12.dll')
		print('File....:APHostClient12.dll')
		print('File....:APHostRes12.dll')
		print('File....:ApnDatabase42.mxl')
		print('File....:AppCapture42.dll')
		print('File....:asferror42.dll')
		print('File....:aspnet_counters42.dll')
		print('poqram....:azman42.msc')
		print('File....:blackbox42.dll')
		print('File....:C_43742.NLS')
		print('File....:C_114442.NLS')
	if command1 == 'open ApnDatabase.xml':
		print('its file unlock')
	if command1 == 'open azman42.msc':
		print('its file unlock')
	if command1 == 'open C_43742.NLS':
		print('its file unlock')
	if command1 == 'open C_114442.NLS':
		print('its file unlock')
	if command1 == 'open aspnet_counters42.dll':
		print('its file unlock')
	if command1 == 'open APHostRes12.dll':
		print('its file unlock')
	if command1 == 'open APHostClient.dll':
		print('its file unlock')
	if command1 == 'open blackbox12.dll':
		print('its file unlock')		
	if command1 == 'open AppCapture42.dll':
		print('its file unlock')		
	if command1 == 'open ApnDatabase.xml':
		print('its file unlock')		
	if command1 == 'open en-US folder':
		print('BlbEvents.dll.mui')
		print('blbres.dll.mui')
		print('bootcfg.exe.mui')
		print('bootux.dll.mui')
		print('browser.dll.mui')
		print('bthserv.dll.mui')	
	if command1 == 'BlbEvents.dll.mui':
		print('not found')
	if command1 == 'bootcfg.exe.mui':
		print('not found')
	if command1 == 'blbres.dll.mui':
		print('not found')
	if command1 == 'bootux.dll.mui':
		print('not found')
	if command1 == 'browser.dll.mui':
		print('not found')
	if command1 == 'bthserv.dll.mui':
		print('not found')
	if command1 == 'open TosBioPlugIns folder':
		print('file enpty')
	if command1 == 'open {127D0A1D-4EF2-11D1-8608-00C04FC295EE}.ini':
		print('not found')
	if command1 == 'open {F750E6C3-38EE-11D1-85E5-00C04FC295EE}.dll':
		print('not found')
	if command1 == 'open FaceRecognitionEngineAdapter.dll':
		print('not found')
	if command1 == 'open FaceRecognitionEngineAdapterResources.dll':
		print('not found')
	if command1 == 'open FaceRecognitionSensorAdapter.dll':
		print('not found')
	if command1 == 'open NUIVoiceWBSAdapters.dll':
		print('not found')
	if command1 == 'open en-US.txt':
		print('not found')
	if command1 == 'open ':
		print('not found')
	if command1 == 'open ':
		print('not found')
	if command1 == 'open ':
		print('not found')
	if command1 == 'open ':
		print('not found')
	if command1 == 'open ':
		print('not found')
	if command1 == 'open ':
		print('not found')
	if command1 == 'open ':
		print('not found')
	if command1 == 'open ApnDatabase.xml':
		print('its file notunlock')
	if command1 == 'open azman42.msc':
		print('its file notunlock')
	if command1 == 'open C_43742.NLS':
		print('its file notunlock')
	if command1 == 'open C_114442.NLS':
		print('its file notunlock')
	if command1 == 'open aspnet_counters42.dll':
		print('its file notunlock')
	if command1 == 'open APHostRes12.dll':
		print('its file notunlock')
	if command1 == 'open APHostClient.dll':
		print('its file notunlock')
	if command1 == 'open blackbox12.dll':
		print('its file notunlock')		
	if command1 == 'open AppCapture42.dll':
		print('its file unlock')		
	if command1 == 'open ApnDatabase.xml':
		print('its file notunlock')		
	if command1 == 'C:/':
		print('RAM......:350mb')
		time.sleep(1)
		print('ROM......:643mb')
		time.sleep(2)
		print('CPU Usage......:10%')
		time.sleep(1)
		print('Doom game......:None')
		time.sleep(1)
		print('Bals game......:None')
		time.sleep(1)
		print('paint......:True')
		time.sleep(2)
		print('CMD......:Open')
		time.sleep(1)
		print('RegEdit......:True')
	if command1 == 'open CatRoot folder':
		print('{127D0A1D-4EF2-11D1-8608-00C04FC295EE}.ini')
		print('{F750E6C3-38EE-11D1-85E5-00C04FC295EE}.dll')
		
	if command1 == 'open TosBioPlugIns folder':
		print('FaceRecognitionEngineAdapter.dll')
		print('FaceRecognitionEngineAdapterResources.dll')
		print('FaceRecognitionSensorAdapter.dll')
		print('NUIVoiceWBSAdapters.dll')
		print('en-US.txt')	

	if command1 == 'open DRVSTORE folder':
		print('file enpty')

	if command1 == 'open en-US folder':
		print('BlbEvents.dll.mui')
		print('blbres.dll.mui')
		print('bootcfg.exe.mui')
		print('bootux.dll.mui')
		print('browser.dll.mui')
		print('bthserv.dll.mui')	

	if command1 == 'BlbEvents.dll.mui':
		print('not found')

	if command1 == 'bootcfg.exe.mui':
		print('not found')

	if command1 == 'blbres.dll.mui':
		print('not found')

	if command1 == 'bootux.dll.mui':
		print('not found')

	if command1 == 'browser.dll.mui':
		print('not found')

	if command1 == 'bthserv.dll.mui':
		print('not found')

	if command1 == 'open TosBioPlugIns folder':
		print('file enpty')

	if command1 == 'open {127D0A1D-4EF2-11D1-8608-00C04FC295EE}.ini':
		print('not found')

	if command1 == 'open {F750E6C3-38EE-11D1-85E5-00C04FC295EE}.dll':
		print('not found')

	if command1 == 'open FaceRecognitionEngineAdapter.dll':
		print('not found')

	if command1 == 'open FaceRecognitionEngineAdapterResources.dll':
		print('not found')

	if command1 == 'open FaceRecognitionSensorAdapter.dll':
		print('not found')

	if command1 == 'open NUIVoiceWBSAdapters.dll':
		print('not found')

	if command1 == 'open en-US.txt':
		print('not found')

	if command1 == 'open ':
		print('not found')

	if command1 == 'calc':
		calc1 = float(input('Ведите 1-ое число: '))
		calc2 = float(input('Ведите 2-ое число: '))
		calc3 = input('дабавте значение(+,-,/,*): ')
		if calc3 == '+':
			answer1 = (calc1 + calc2)
			print(answer1)
			print('Решено')

		if calc3 == '-':
			answer1 = (calc1 - calc2)
			print(answer1)
			print('Решено')

		if calc3 == '*':
			answer1 = (calc1 * calc2)
			print(answer1)
			print('Решено')

		if calc3 == '/':
			answer1 = (calc1 / calc2)
			print(answer1)
			print('Решено')

		command1 = input("C:RegEdit:")
		print('Folder....:Tonibrozz')
		time.sleep(1)
		print('Folder....:TanOs3')
		time.sleep(1)
		print('Folder....:system42')
		if command1 == 'open Tonibrozz folder':
			print('Folder....:0409')
			print('Folder....:AdvancedInstallers')
			print('Folder....:appmgmt')
			print('Folder....:CatRoot')
			print('Folder....:DRVSTORE')
			print('Folder....:en-US')
			print('Folder....:ru-RU')
			print('Folder....:TosBioPlugIns')


		if command1 == 'open 0409 folder':
			print('Folder....:Assets')
			print('Folder....:pris')
			print('File....:appxblockmap.xml')
			print('File....:appxmanifest.xml')
			print('File....:MiracastView.dll')
			

		if command1 == 'open AdvancedInstallers folder':
			print('Folder....:Tlash')


		if command1 == 'open Tlash folder':
			print('File....:activex.vch')
			print('File....:Flash.ocx')
			print('File....:FlashUtil_ActiveX.dll')
		

		if command1 == 'open activex.vch':
			print('file not found')
			
		if command1 == 'open Flash.ocx':
			print('file not found')
		
		if command1 == 'open FlashUtil_ActiveX.dll':
			print('file not found')



		if command1 == 'open appmgmt folder':
			print('File enpty')
			


		if command1 == 'open CatRoot folder':
			print('File...:{127D0A1D-4EF2-11D1-8608-00C04FC295EE}.txt')
			print('File...:{F750E6C3-38EE-11D1-85E5-00C04FC295EE}.txt')


		if command1 == 'open TosBioPlugIns folder':
			print('FaceRecognitionEngineAdapter.dll')
			print('FaceRecognitionEngineAdapterResources.dll')
			print('FaceRecognitionSensorAdapter.dll')
			print('NUIVoiceWBSAdapters.dll')
			print('en-US.txt')			


		if command1 == 'open TanOs4 folder':
			print('Folder....:Recovery')


		if command1 == 'open Recovery folder':
			print('File....:Recovery.dat')


		if command1 == 'open Recovery.dat':
			print('file enoty')


	if command1 == 'open ApnDatabase.xml':
		print('its file unlock')


	if command1 == 'open azman42.msc':
		print('its file unlock')


	if command1 == 'open C_43742.NLS':
		print('its file unlock')


	if command1 == 'open C_114442.NLS':
		print('its file unlock')


	if command1 == 'open aspnet_counters42.dll':
		print('its file unlock')


	if command1 == 'open APHostRes12.dll':
		print('its file unlock')


	if command1 == 'open APHostClient.dll':
		print('its file unlock')


	if command1 == 'open blackbox12.dll':
		print('its file unlock')	


	if command1 == 'open AppCapture42.dll':
		print('its file unlock')


	if command1 == 'open ApnDatabase.xml':
		print('its file unlock')	


	if command1 == 'open D:':
			print('Folder....:TosBioPlugIns')
			print('FaceRecognitionEngineAdapter.dll')
			print('FaceRecognitionEngineAdapterResources.dll')
			print('FaceRecognitionSensorAdapter.dll')
			print('NUIVoiceWBSAdapters.dll')
			print('en-US.txt')
			print('Folder....:Assets')
			print('Folder....:pris')
			print('File....:appxblockmap.xml')
			print('File....:appxmanifest.xml')
			print('File....:MiracastView.dll')
			print('BlbEvents.dll.mui')
			print('blbres.dll.mui')
			print('bootcfg.exe.mui')
			print('bootux.dll.mui')
			print('Folder....:0409')
			print('Folder....:AdvancedInstallers')
			print('Folder....:ru-RU')
			print('browser.dll.mui')
			print('bthserv.dll.mui')	
			print('{127D0A1D-4EF2-11D1-8608-00C04FC295EE}.ini')
			print('{F750E6C3-38EE-11D1-85E5-00C04FC295EE}.dll')
			print('BlbEvents.dll.mui')
			print('blbres.dll.mui')
			print('bootcfg.exe.mui')
			print('bootux.dll.mui')
			print('browser.dll.mui')
			print('bthserv.dll.mui')	
			print('Folder....:appmgmt')
			print('Folder....:CatRoot')
			print('Folder....:DRVSTORE')
			print('Folder....:en-US')
			print('Foile....:apds.dll')
			print('Foile....:APHostClient.dll')
			print('Foile....:APHostRes.dll')
			print('Foile....:ApnDatabase.xml')
			print('Foile....:AppCapture.dll')
			print('Foile....:asferror.dll')
			print('Foile....:aspnet_counters.dll')
			print('proqram....:azman.msc')
			print('File....:blackbox12.dll')
			print('File....:C_43712.NLS')
			print('File....:C_114412.NLS')
			print('File....:apds12.dll')
			print('File....:APHostClient12.dll')
			print('File....:APHostRes12.dll')
			print('File....:ApnDatabase42.mxl')
			print('File....:AppCapture42.dll')
			print('File....:asferror42.dll')
			print('File....:aspnet_counters42.dll')
			print('poqram....:azman42.msc')
			print('Folder....:blackbox42.dll')
			print('File....:C_43742.NLS')
			print('File....:C_114442.NLS')
		
	if command1 == 'azman.msc':
		print('not found')

	if command1 == 'blackbox42.dll':
		print('cdosys.dll.mui')
		print('comctl32.dll.mui')
		print('comdlg32.dll.mui')
		print('fms.dll.mui')
		print('mlang.dll.mui')
		print('msimsg.dll.mui')
		print('windows.ui.xaml.dll.mui')
		print('WWAHost.exe.mui')

	if command1 == 'cdosys.dll.mui':
		print('not found')

	if command1 == 'comdlg32.dll.mui':
		print('not found')

	if command1 == 'windows.ui.xaml.dll.mui':
		print('not found')

	if command1 == 'fms.dll.mui':
		print('not found')
	
	if command1 == 'msimsg.dll.mui':
		print('not found')
	
	if command1 == 'WWAHost.exe.mui':
		print('not found')

	if command1 == 'aspnet_counters.dll':
		print('cdosys.dll.mui')
		print('comctl32.dll.mui')
		print('comdlg32.dll.mui')
		print('fms.dll.mui')
		print('mlang.dll.mui')
		print('msimsg.dll.mui')
		print('windows.ui.xaml.dll.mui')
		print('WWAHost.exe.mui')

	if command1 == 'cdosys.dll.mui':
		print('not found')

	if command1 == 'comdlg32.dll.mui':
		print('not found')

	if command1 == 'windows.ui.xaml.dll.mui':
		print('not found')

	if command1 == 'fms.dll.mui':
		print('not found')
	
	if command1 == 'msimsg.dll.mui':
		print('not found')
	
	if command1 == 'WWAHost.exe.mui':
		print('not found')


	
	if command1 == 'open 0409 folder':
	
		print('Folder....:Assets')
	
		print('Folder....:pris')
	
		print('File....:appxblockmap.xml')
	
		print('File....:appxmanifest.xml')
	
		print('File....:MiracastView.dll')
	


	
	if command1 == 'open AdvancedInstallers folder':
	
		print('Folder....:Tlash')

	
	if command1 == 'open Tlash folder':
	
		print('File....:activex.vch')
	
		print('File....:Flash.ocx')
	
		print('File....:FlashUtil_ActiveX.dll')
	

	
	if command1 == 'open activex.vch':
	
		print('file not found')
	

	
	if command1 == 'open Flash.ocx':
	
		print('file not found')
	

	
	if command1 == 'open FlashUtil_ActiveX.dll':
	
		print('file not found')

	
	if command1 == 'open appmgmt folder':
	
		print('File enpty')
	


	
	if command1 == 'open CatRoot folder':
	
		print('File...:{127D0A1D-4EF2-11D1-8608-00C04FC295EE}.txt')
	
		print('File...:{F750E6C3-38EE-11D1-85E5-00C04FC295EE}.txt')

	
	if command1 == 'open TosBioPlugIns folder':
	
		print('FaceRecognitionEngineAdapter.dll')
	
		print('FaceRecognitionEngineAdapterResources.dll')
	
		print('FaceRecognitionSensorAdapter.dll')
	
		print('NUIVoiceWBSAdapters.dll')
	
		print('en-US.txt')			

	
	if command1 == 'open TanOs4 folder':
	
		print('Folder....:Recovery')

	
	if command1 == 'open Recovery folder':
	
		print('File....:Recovery.dat')

	
	if command1 == 'open Recovery.dat':
			print('file enoty')


	if command1 == 'open ApnDatabase.xml':
		print('its file unlock')


	if command1 == 'open azman42.msc':
		print('its file unlock')


	if command1 == 'open C_43742.NLS':
		print('its file unlock')


	if command1 == 'open C_114442.NLS':
		print('its file unlock')


	if command1 == 'open aspnet_counters42.dll':
		print('its file unlock')


	if command1 == 'open APHostRes12.dll':
		print('its file unlock')


	if command1 == 'open APHostClient.dll':
		print('its file unlock')


	if command1 == 'open blackbox12.dll':
		print('its file unlock')	


	if command1 == 'open AppCapture42.dll':
		print('its file unlock')


	if command1 == 'open ApnDatabase.xml':
		print('its file unlock')	
	


