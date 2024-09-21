import unittest
from unittest.mock import patch
from troubleshooting import Troubleshooting

class TestTroubleshooting(unittest.TestCase):

    @patch('troubleshooting.Troubleshooting.run_command')
    def test_check_pod_status(self, mock_run_command):
        # Simulamos la salida que esperamos de kubectl
        mock_run_command.return_value = "NAME        READY   STATUS    RESTARTS   AGE\npod-1       1/1     Running   0          10m"

        ts = Troubleshooting()
        result = ts.check_pod_status(namespace="default")

        # Verificamos que se ejecutó el comando correcto
        mock_run_command.assert_called_once_with("kubectl get pods -n default -o wide")

        # Verificamos que el resultado sea el esperado
        self.assertEqual(result, "NAME        READY   STATUS    RESTARTS   AGE\npod-1       1/1     Running   0          10m")

if __name__ == '__main__':
    unittest.main()
