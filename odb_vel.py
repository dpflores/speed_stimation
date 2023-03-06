import time
import os
import can

# In the extension we shall bring up the interfaces directly within our Python app
os.system("sudo /sbin/ip link set can0 down")
time.sleep(1)

os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
time.sleep(1)


# set up a CAN bus
bus = can.interface.Bus(channel="can0", bustype='socketcan')


# using defaults functional address
obd2_tx_arb_id = 0x7DF
obd2_rx_arb_id = 0x7E8

# CAN Frame for a PID Request of 0x0C (RPM) with SAE Standard
#obd_req_data = [2, 1, 0x0C, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC]
while True:
    #time.sleep(0.5)
    try:
        obd_req_data_velocidad = [2, 1, 0x0D, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC]
        # Send our OBD-II query in CAN 11-bit format
        msg_velocidad = can.Message(arbitration_id=obd2_tx_arb_id, data=obd_req_data_velocidad, is_extended_id=False)
        bus.send(msg_velocidad)
        #print("ok 1")
        message_velocidad = bus.recv(timeout=1.0) # Timeout in seconds.
        #print(message_velocidad.arbitration_id)
        #print(message_velocidad.data)
        if message_velocidad is None:
            print('Timeout occurred, no message.')
            #sys.exit(1)

        # Check if received the expected response message
        if message_velocidad.arbitration_id == 2024: #obd2_rx_arb_id:
            #print("Message received VELOCITY")
            #print(message.data)
            hex_data_velocidad = ""
            i=0
            a_velocity_1=0
            for c in message_velocidad.data:
                i=i+1
                hex_data_velocidad += "%02X " % c
                if i==4:
                    a_velocity= c
                    a_velocity_1=int(c)
                    #print(a_velocity)
            print("VELOCIDAD: ", a_velocity_1)
            #print("Response ID: %03X | Response Data: %s" % (message_velocidad.arbitration_id, hex_data_velocidad))
    except:
        pass

    