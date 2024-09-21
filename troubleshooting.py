import subprocess

class Troubleshooting:
    
    def __init__(self):
        pass

    def run_command(self, command):
        """Helper function to run shell commands."""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout
            else:
                return f"Error: {result.stderr}"
        except Exception as e:
            return f"Command execution failed: {e}"

    # Kubernetes Troubleshooting
    def check_pod_status(self, namespace="default"):
        """Check the status of all pods in a given namespace."""
        command = f"kubectl get pods -n {namespace} -o wide"
        return self.run_command(command)

    def describe_pod(self, pod_name, namespace="default"):
        """Describe a specific pod to get more detailed information."""
        command = f"kubectl describe pod {pod_name} -n {namespace}"
        return self.run_command(command)

    def check_container_logs(self, pod_name, namespace="default", container_name=None):
        """Check the logs of a container within a pod."""
        container_arg = f"-c {container_name}" if container_name else ""
        command = f"kubectl logs {pod_name} -n {namespace} {container_arg}"
        return self.run_command(command)

    def check_service(self, service_name, namespace="default"):
        """Check the status of a Kubernetes service."""
        command = f"kubectl get svc {service_name} -n {namespace} -o wide"
        return self.run_command(command)

    def check_deployments(self, namespace="default"):
        """Check the status of all deployments in a namespace."""
        command = f"kubectl get deployments -n {namespace} -o wide"
        return self.run_command(command)

    # Networking Troubleshooting
    def check_network_policy(self, namespace="default"):
        """Check the network policies applied in a namespace."""
        command = f"kubectl get networkpolicies -n {namespace}"
        return self.run_command(command)

    def ping_service(self, service_name, namespace="default"):
        """Ping a service IP to verify its network reachability."""
        command = f"kubectl get svc {service_name} -n {namespace} -o jsonpath='{{.spec.clusterIP}}'"
        service_ip = self.run_command(command).strip()
        if "Error" not in service_ip:
            return self.run_command(f"ping -c 3 {service_ip}")
        return f"Failed to retrieve service IP: {service_ip}"

    def check_dns_resolution(self, pod_name, namespace="default"):
        """Check if DNS resolution is working inside a pod."""
        command = f"kubectl exec {pod_name} -n {namespace} -- nslookup kubernetes.default"
        return self.run_command(command)

    def check_pod_connectivity(self, pod_name, target_ip, namespace="default"):
        """Check connectivity from a pod to a target IP address."""
        command = f"kubectl exec {pod_name} -n {namespace} -- ping -c 3 {target_ip}"
        return self.run_command(command)

    # DNS Troubleshooting
    def check_core_dns_pod_status(self):
        """Check if the CoreDNS pods are running correctly."""
        command = "kubectl get pods -n kube-system -l k8s-app=kube-dns -o wide"
        return self.run_command(command)

    def restart_core_dns(self):
        """Restart the CoreDNS service to resolve DNS issues."""
        command = "kubectl rollout restart deployment/coredns -n kube-system"
        return self.run_command(command)

    def check_dns_service(self):
        """Check the status of the DNS service in the cluster."""
        command = "kubectl get svc kube-dns -n kube-system -o wide"
        return self.run_command(command)

    # Container Troubleshooting
    def check_container_restart_count(self, pod_name, namespace="default"):
        """Check how many times a container has been restarted."""
        command = f"kubectl get pod {pod_name} -n {namespace} -o jsonpath='{{.status.containerStatuses[*].restartCount}}'"
        return self.run_command(command)

    def check_container_status(self, pod_name, namespace="default"):
        """Check the detailed status of all containers in a pod."""
        command = f"kubectl get pod {pod_name} -n {namespace} -o jsonpath='{{.status.containerStatuses[*]}}'"
        return self.run_command(command)

    # General cluster troubleshooting
    def check_cluster_nodes(self):
        """Check the status of all nodes in the cluster."""
        command = "kubectl get nodes -o wide"
        return self.run_command(command)

    def check_events(self, namespace="default"):
        """Check Kubernetes events in a given namespace."""
        command = f"kubectl get events -n {namespace} --sort-by=.metadata.creationTimestamp"
        return self.run_command(command)

    def check_cluster_info(self):
        """Retrieve basic information about the Kubernetes cluster."""
        command = "kubectl cluster-info"
        return self.run_command(command)
    
    def check_control_plane_nodes(self):
        components = ["kube-apiserver", "kube-controller", "kube-scheduler"]
        control_plane_namespace = "kube-system"
        output = ""
        for component in components:
            output += f"checking {component}...\n"
            pod_command = f"kubectl get pods -n {control_plane_namespace} -l component={component}"
            pod_command_output = self.run_command(pod_command)
            output += f"Pod for {component}:\n{pod_command_output}\n"
        return output