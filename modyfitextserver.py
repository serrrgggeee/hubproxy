from twisted.internet import reactor, protocol, endpoints
import re


class UpperProtocol(protocol.Protocol):

	def connectionMade(self):
		pass

	def connectionLost(self, reason):
		pass

	def dataReceived(self, data):
		div = re.sub(r'<[^>]*>(\w{6})<\/[^>]*>', "\\1тм", data.decode("utf-8"), re.MULTILINE | re.DOTALL)
		self.transport.write(div.encode("utf-8"))
		self.transport.loseConnection()


factory = protocol.ServerFactory()
factory.protocol = UpperProtocol
reactor.listenTCP(8000, factory)
reactor.run()		