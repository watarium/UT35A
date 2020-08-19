from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.1.1', port=502)
client.connect()

result = client.read_holding_registers(address=2001, count=1, unit=1)
print(result.registers[0]/10)