from smc100 import SMC100

smc_port = 'COM8'
sr830m_port = 'COM7'
output_file = "test.txt"


sr830m = serial.Serial(
        port = sr830m_port,
        baudrate = 19200,
        bytesize = 8,
        stopbits = 1,
        parity = 'N',
        xonxoff = True,
        timeout = 0.050)

smc100_1 = SMC100(1, smc_port, silent=False)
sleep(1)
smc100_1.move_absolute_um(-125000)
sleep(1)

g=open(output_file,"w+")
tosend1 = 'OUTP? 3'

for i in range(5):
    position1 = -125000+10000*i
    #print("position",position1)
    smc100_1.move_absolute_um( position1 )
    sleep(0.5)  

    sr830m.flushInput() #This may not be required
    sr830m.flushOutput()#This may not be required
    sr830m.write(tosend1.encode())
    sr830m.write(b'\n')
    sleep(.1) # In case if device is slow to respond
    res = _port1.read(5)
    g.write("%s\n %s\n " % position1 %res)
    sr830m.flush() 

    g.write("%s\n" % position1)
    sleep(1)

g.close()        
sr830m.close()
del smc100_1
#sleep(2)    




