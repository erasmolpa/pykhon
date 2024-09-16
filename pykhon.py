import click
from troubleshooting import Troubleshooting  # Importa la clase que creaste

# Instanciamos la clase Troubleshooting para usar sus métodos
ts = Troubleshooting()

@click.group()
def cli():
    """CLI para realizar troubleshooting de Kubernetes, Containers, Pods, Services, Networking y DNS"""
    pass

# Definir comandos CLI para cada función del Troubleshooting

@cli.command()
@click.option('--namespace', default='default', help='Namespace a consultar')
def check_pod_status(namespace):
    """Verificar el estado de los pods en un namespace"""
    result = ts.check_pod_status(namespace)
    click.echo(result)


@cli.command()
@click.argument('pod_name')
@click.option('--namespace', default='default', help='Namespace del pod')
def describe_pod(pod_name, namespace):
    """Describir un pod específico"""
    result = ts.describe_pod(pod_name, namespace)
    click.echo(result)


@cli.command()
@click.argument('pod_name')
@click.option('--namespace', default='default', help='Namespace del pod')
@click.option('--container_name', default=None, help='Nombre del contenedor (opcional)')
def check_container_logs(pod_name, namespace, container_name):
    """Ver logs de un contenedor dentro de un pod"""
    result = ts.check_container_logs(pod_name, namespace, container_name)
    click.echo(result)


@cli.command()
@click.argument('service_name')
@click.option('--namespace', default='default', help='Namespace del servicio')
def check_service(service_name, namespace):
    """Verificar el estado de un servicio en Kubernetes"""
    result = ts.check_service(service_name, namespace)
    click.echo(result)


@cli.command()
@click.option('--namespace', default='default', help='Namespace a consultar')
def check_deployments(namespace):
    """Verificar el estado de los deployments en un namespace"""
    result = ts.check_deployments(namespace)
    click.echo(result)


@cli.command()
@click.option('--namespace', default='default', help='Namespace a consultar')
def check_network_policy(namespace):
    """Verificar las políticas de red en un namespace"""
    result = ts.check_network_policy(namespace)
    click.echo(result)


@cli.command()
@click.argument('service_name')
@click.option('--namespace', default='default', help='Namespace del servicio')
def ping_service(service_name, namespace):
    """Hacer ping a la IP de un servicio"""
    result = ts.ping_service(service_name, namespace)
    click.echo(result)


@cli.command()
@click.argument('pod_name')
@click.option('--namespace', default='default', help='Namespace del pod')
def check_dns_resolution(pod_name, namespace):
    """Verificar la resolución DNS dentro de un pod"""
    result = ts.check_dns_resolution(pod_name, namespace)
    click.echo(result)


@cli.command()
@click.argument('pod_name')
@click.argument('target_ip')
@click.option('--namespace', default='default', help='Namespace del pod')
def check_pod_connectivity(pod_name, target_ip, namespace):
    """Verificar la conectividad desde un pod hacia una IP objetivo"""
    result = ts.check_pod_connectivity(pod_name, target_ip, namespace)
    click.echo(result)


@cli.command()
def check_core_dns_pod_status():
    """Verificar el estado de los pods de CoreDNS"""
    result = ts.check_core_dns_pod_status()
    click.echo(result)


@cli.command()
def restart_core_dns():
    """Reiniciar el servicio CoreDNS"""
    result = ts.restart_core_dns()
    click.echo(result)


@cli.command()
def check_dns_service():
    """Verificar el estado del servicio DNS"""
    result = ts.check_dns_service()
    click.echo(result)


@cli.command()
@click.argument('pod_name')
@click.option('--namespace', default='default', help='Namespace del pod')
def check_container_restart_count(pod_name, namespace):
    """Verificar cuántas veces se ha reiniciado un contenedor"""
    result = ts.check_container_restart_count(pod_name, namespace)
    click.echo(result)


@cli.command()
@click.argument('pod_name')
@click.option('--namespace', default='default', help='Namespace del pod')
def check_container_status(pod_name, namespace):
    """Verificar el estado de los contenedores dentro de un pod"""
    result = ts.check_container_status(pod_name, namespace)
    click.echo(result)


@cli.command()
def check_cluster_nodes():
    """Verificar el estado de todos los nodos en el clúster"""
    result = ts.check_cluster_nodes()
    click.echo(result)


@cli.command()
@click.option('--namespace', default='default', help='Namespace a consultar')
def check_events(namespace):
    """Verificar eventos recientes en un namespace"""
    result = ts.check_events(namespace)
    click.echo(result)


@cli.command()
def check_cluster_info():
    """Obtener información básica del clúster de Kubernetes"""
    result = ts.check_cluster_info()
    click.echo(result)


if __name__ == '__main__':
    cli()
