import socket
import binascii


def send_data(data_list):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('192.168.1.1', 502))
        for i in range(len(data_list)):
            # send data
            data = bytes.fromhex(data_list[i])
            s.send(data)
            data = s.recv(1024)

            # receive data
            received_hex_data = binascii.hexlify(data)
            print(received_hex_data)
        s.close()

data_dict = {}
# data_dict['data_list0'] = ['00000000000a0167000100044f580001']
# data_dict['data_list1'] = ['00000000000a016700010004139a0002']
# data_dict['data_list2'] = ['0000000000ce0167003200c8138a0000138c0000138e000413900004139300001395000413ec000113ed000113ef358413f0f57413ef358413f0f57413f4000113f5000113f6000013f7000013f800001450000114510001145235841453f574145235841453f57414593584145af57414593584145af57414b4000314b6001e14c8000114c9358414caf57414c9358414caf57414cb000014dc000014de000014e60000164400001645000016460017164700011650000016560005165800a4165a10e1165b10e2165c10e3165d10e5166a0001','0000000000ce0167003200c8166b0001166c0001166d0004166e0001166f0000167000001671000316720000167300001674000016750000167600001678000216790001167a0000167d0000168000001681000016820000168300001684000016890000168a0000168b0000168c0000168d0000168e0000168f000016900000169100001692000016a8000016aa000016ac000016ad000016ae000116b0000116b2000016b5000116c6000016c7000016cb000016cd000016d2000016d6000016d7000016d8000016d9000016da000016db0000','0000000000ce0167003200c816dc000016e1000016e6000016e7000016e8000016e9000016ea000016eb000016ec000016ed000016ee000016ef000016f1000016f2000016f3000016f4000016fc0000170c13a1170d0000170f13a21711000017120000171300001714000017190000171f000017200000173000001721000017220000172300001724000017700000177100001772000017730000177400001775000017760000177700001778000017790000177a0000178400001785000017860000178700001788000017890000178a0000','0000000000ce0167003200c8178b0000178c0000178d0000178e00001798000017990000179a0000179b0000179c0000179d0000179e0000179f000017a0000017a1000017a2000017ac000017ad000017ae000017af000017b0000017b1000017b2000017b3000017b4000017b5000017b60000173500001736000017370000173b0000173c0000173d00001748000017490000174a000017340000173a00001747000017d4000017d500001838110118391102183a1103183b0000183d0000183e0000183f0000184000001900000019010000','0000000000ce0167003200c81907000019080000190900001910000019110000191e00020af000010af100000af200000af300000af400020af500000af600000af700000af800010af900000afa00000afb00000afc00020afd00000afe00000aff00000b10003c0b11003c0b12003c0b13003c0b18000a0b19000a0b1a000a0b1b000a0b2000000b2100000b2200000b2300000b2800000b2900000b2a00000b2b00000b31000009c4012c09c6000109c7000009c8000009c9000009ca000009d8f57409da000209db000009dc000009dd0000','0000000000ce0167003200c809de000009ecf57409ee000309ef000009f0000009f1000009f200000a00f5740a0200040a0300000a0400000a0500000a0600000a8e03e80a8f00000a9000000a9100000a9200000a9500010a9600000b5400000b5500000bb800050bb9003c0bba00000bbb03e80bbc00000bbd01f40bc200000bcb00000bea00320beb00f00bec003c0bed03e80bee00000bef01f40bf400000bfd00000c1c00320c1d00f00c1e003c0c1f03e80c2000000c2101f40c2600000c2f00000c4e00320c4f00f00c50003c0c5103e8','0000000000ce0167003200c80c5200000c5301f40c5800000c6100000dac00000dae00000daf03e80db000000db100000dc500000dc600000dc700010dca00000dcb00000dcc00000dcd00000dce00000dcf00000dde35840ddf35840de035840de500520de60000125c0000125d0000125e0000125f0000126000001261000012620000126300001264000012650000127000001271000012720000127300001274000012750000127600001277000012780000127900004f606c614f6164644f6261724f635f774f6461744f6561724f666975','0000000000420167000f003c4f676d004f6800004f6900004f6a00004f6b00004f6c00004f6d00004f6e00004f6f00004f7000004f7100004f7200004f7300004f7400004f4e0409']
# data_dict['data_list3'] = ['00000000001201670003000c4f5d00014f5c00014f5e0001']
# data_dict['data_list4'] = ['00000000006b016559d80032640a25008107630001076b008a000000c9000000fe0a250081000000fb08250001082d008a000000c9000000fc08270001082f008a000000c9000000fc082900010830008a000000c9000000fd082800010831008a000000c90a250081000000fb08090001','00000000005301655a0a00264c0833008a000000c9000000fc080d00010837008a000000c9000000fd081f00010849008a000000c9000000f90aac00820aab01400aab00810a3200010277008a000000c9000000ff0000007f']
# data_dict['data_list5'] = ['0000000000ce0167003200c84f8874654f8973744f8a32004f8b00004f8c00004f7e00004f7f00004f8000004f8100004f8200004f5000054f510026501400005015000050160000501700005018000050190000501a0000501b0000501c0000501d0000501e0000501f000050200000502100005022000050230000502400005025000050260000502700005028000050290000502a0000502b0000502c0000502d0000502e0000502f000050300000503100001c8400001c8500001c8600001c8700001c8800001c8900001c8a00001c8b0000','00000000005e0167001600581c8c00001c8d00001c8e00001c8f00001c9000001c9100001c9200001c9300001c9400001c9500001c9600001c9700001c9800001c9900001c9a00001c9b00001c9c00001c9d00001c9e00001c9f00001ca000001ca10000']
# data_dict['data_list6'] = ['00000000008e016700220088159100061592000115a40001159100061592000115a700c015a800a815a9000115aa000115ab00ff15ac00ff15ad00ff15ae000015af000015b0000015b1000015b2000015b301f615b4000015b500ff15b600ff15b700ff15b800ff15b900ff15ba00ff15bb00ff15bc00ff16ba000016bb00001709000115bd00014f5d00004f58000016b90000']

# 100% ON after 100 seconds.
data_dict['data_list0'] = ['000000000017016600091213884f524f5407d00813081507db139a16b9','00000000000a0167000100044f580001','00000000001201670003000c4f5d00014f5c00014f5e0001','00000000006b016559d80032640a25008107630001076b008a000000c9000000fe0a250081000000fb08250001082d008a000000c9000000fc08270001082f008a000000c9000000fc082900010830008a000000c9000000fd082800010831008a000000c90a250081000000fb08090001','00000000006b01655a0a0032640833008a000000c9000000fc080d00010837008a000000c9000000fd081f00010849008a000000c9000000f90a240082000000fb0a29008a0b33008a0a3b000100000132000000fd0a3e00010a5a008a000000c90b3300810a3b00010830008a000000c9','00000000000f01655a3c000408000000ff0000007f','0000000000ce0167003200c84f8874654f8973744f8a32004f8b00004f8c00004f7e00004f7f00004f8000004f8100004f8200004f5000054f51002e501400005015000050160000501700005018000050190000501a0000501b0000501c0000501d0000501e0000501f000050200000502100005022000050230000502400005025000050260000502700005028000050290000502a0000502b0000502c0000502d0000502e0000502f000050300000503100001c8400001c8500001c8600001c8700001c8800001c8900001c8a00001c8b0000','0000000000660167001800601c8c00001c8d00001c8e00001c8f00001c9000001c9100001c9200001c9300001c9400001c9500001c9600001c9700001c9800001c9900001c9a00001c9b00001c9c00001c9d00001c9e00001c9f00001ca000001ca100004f5d00004f580000']

for i in range(len(data_dict)):
    send_data(data_dict['data_list'+str(i)])