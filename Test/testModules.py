import unittest
import sys

from unittest.mock import patch, MagicMock

sys.path.append("..")


from Semabox import InfoServer

class TestInfoServer(unittest.TestCase):
    @patch('Semabox.Modules.Information.info.platform.node')
    def test_get_hostname(self, mock_node):
        mock_node.return_value = 'test_hostname'
        self.assertEqual(InfoServer.get_hostname(), 'test_hostname')

    @patch('Semabox.Modules.Information.info.socket.gethostbyname')
    @patch('Semabox.Modules.Information.info.socket.gethostname')
    def test_get_ip_address(self, mock_gethostname, mock_gethostbyname):
        mock_gethostname.return_value = 'test_hostname'
        mock_gethostbyname.return_value = '1.2.3.4'
        self.assertEqual(InfoServer.get_ip_address(), '1.2.3.4')

    def test_get_address_network(self):
        ip = '1.2.3.4'
        expected_network = '1.2.3.0/24'
        self.assertEqual(InfoServer.get_address_network(ip), expected_network)

    @patch('Semabox.Modules.Information.info.socket.gethostbyaddr')
    @patch('Semabox.InfoServer.get_ip_address')
    def test_get_dns(self, mock_get_ip_address, mock_gethostbyaddr):
        mock_get_ip_address.return_value = '1.2.3.4'
        mock_gethostbyaddr.return_value = ('test_dns', [], [])
        self.assertEqual(InfoServer.get_dns(), 'test_dns')

    @patch('Semabox.Modules.Information.info.requests.get')
    def test_get_public_ip(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'ip': '1.2.3.4'}
        mock_requests_get.return_value = mock_response
        self.assertEqual(InfoServer.get_public_ip(), '1.2.3.4')

    def test_api_get_public_ip(self):
        ip = '1.2.3.4'
        expected_result = {'ip_public': ip}
        self.assertEqual(InfoServer.api_get_public_ip(ip), expected_result)
        
            
    @patch('Semabox.InfoServer.get_hostname')
    @patch('Semabox.InfoServer.get_ip_address')
    @patch('Semabox.InfoServer.get_dns')
    @patch('Semabox.InfoServer.get_version_semabox')
    @patch('Semabox.InfoServer.get_public_ip')
    def test_api_info_server(self, mock_get_public_ip, mock_get_version_semabox, mock_get_dns, mock_get_ip_address, mock_get_hostname):
        mock_get_hostname.return_value = 'test_hostname'
        mock_get_ip_address.return_value = '1.2.3.4'
        mock_get_dns.return_value = 'test_dns'
        mock_get_version_semabox.return_value = 'test_version'
        mock_get_public_ip.return_value = '5.6.7.8'

        expected_result = {
            'hostname': 'test_hostname',
            'ip': '1.2.3.4',
            'ip_public': '5.6.7.8',
            'dns': 'test_dns',
            'uid': 'test_uid',
            'version_semabox': 'test_version'
        }

        self.assertEqual(InfoServer.api_info_server(uid='test_uid'), expected_result)

if __name__ == '__main__':
    unittest.main()