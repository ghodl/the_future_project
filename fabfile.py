import os
from fabric.api import local, run, cd, env, sudo, settings, lcd
from fabric.decorators import hosts

env.hosts = [
    "sama@beeola.tuteria.com"
    # 'sama@tutor-search.tuteria.com'
]
password = os.getenv("PRODUCTION_PASSWORD", "")


def common_code(code_dir, script, proceed=True, branch="master"):
    with settings(user="sama", password=password):
        with cd(code_dir):
            run("pwd")
            run("git checkout -f %s" % branch)
            if "code" in code_dir:
                run("git pull -f")
            else:
                run("git pull -f")
            run(script)


@hosts("sama@beeola.tuteria.com")
def deploy_current(branch="master"):
    print("hello World")
    run("pwd")
    code_dir = "/home/sama/code/future-project"
    common_code(code_dir, "./boot_app.sh", branch=branch)

@hosts("sama@backup.tuteria.com")
def backup_db():
    with settings(user="sama", password=password):
        run("/home/sama/tuteria/deploy/postgres-backup.sh")



@hosts("sama@beeola.tuteria.com")
def w_images():
    with cd("/home/sama/tuteria"):
        # run("git pull upstream master")
        run("docker-compose pull app")
        run("docker-compose kill app2")
        run("docker-compose rm -f app2")
        # run("docker-compose run app2 python manage.py collectstatic --noinput")
        run("docker-compose up -d --scale app2=2 app2")
        run('docker rmi $(docker images --filter "dangling=true" -q --no-trunc)')


