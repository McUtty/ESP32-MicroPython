def connect():
    import network
    import wlanscan
    from time import sleep_ms

    netscan = wlanscan.WLANscan()
    ssidlist = netscan.ssid()


    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        print('Searching for Network...')
        sta_if.active(True)

        for net in ssidlist:
            #print(net)
            if net == 'UT-VNet':
                sta_if.connect('WLAN', 'xxxPASSWORDxxx')
                while not sta_if.isconnected():
                    print('connecting ...')
                    sleep_ms(500)
                break

            if str(net) == 'Taubald':
                sta_if.connect('Taubald', '62846088313536200468')
                while not sta_if.isconnected():
                    print('connecting ...')
                    sleep_ms(500)
                break

    if not sta_if.isconnected():
        print('Kein bekanntes Netzwerk gefunden')
    else:
        print('Network connected:', sta_if.ifconfig())

def no_debug():
    import esp
    esp.osdebug(None)

def disconnect():
	import network
	sta_if = network.WLAN(network.STA_IF)
	sta_if.disconnect()

no_debug()
connect()
