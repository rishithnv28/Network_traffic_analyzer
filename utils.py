def suspicious_packet(packet):
    try:
        if 'TCP' in packet:
            tcp_layer = packet.tcp
            if tcp_layer.flags == '0x002':
                return "SYN scan detected"
        if 'DNS' in packet:
            dns_layer = packet.dns
            if dns_layer.qr == '0' and dns_layer.opcode == '0':
                return "Potential DNS tunneling"
    except AttributeError:
        return None
    return None
