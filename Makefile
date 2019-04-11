IMAGE=docker.io/sitoi/flask-template:latest
GITHUB_URL=https://github.com/Sitoi/Flask-Template.git
PROJECT_NAME=flask-template
BRANCH=master
NAMESPACE=shitao

.PHONY: build push save load test


build:
	docker-compose build --no-cache

push: build
	docker push $(IMAGE)

save: build
	docker save -o $(PROJECT_NAME).tar $(IMAGE)

load:
	docker load --input $(PROJECT_NAME).tar

test:
	pytest --cov=app tests/  --cov-report=html --disable-warnings

deploy:
	oc new-app $(GITHUB_URL)#$(BRANCH) --env-file=config.env --allow-missing-images=true --name=$(PROJECT_NAME) -n $(NAMESPACE)

destroy:
	oc delete all -l app=$(PROJECT_NAME) -n $(NAMESPACE)

start:
	oc start-build bc/${PROJECT_NAME} -n $(NAMESPACE)