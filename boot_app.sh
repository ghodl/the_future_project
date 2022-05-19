cd /home/sama/code/future-project && docker build -f compose/production/django/Dockerfile -t=registry.gitlab.com/gbozee/future-project .
docker push registry.gitlab.com/gbozee/future-project 
cd /home/sama/code/future-project && docker build -f compose/production/postgres/Dockerfile -t=registry.gitlab.com/gbozee/future-project/db .
docker push registry.gitlab.com/gbozee/future-project/db 
cd /home/sama/code/future-project && docker build -f compose/production/traefik/Dockerfile -t=registry.gitlab.com/gbozee/future-project/lb .
docker push registry.gitlab.com/gbozee/future-project/lb