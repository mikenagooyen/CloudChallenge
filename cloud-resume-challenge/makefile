.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec mnguyen --no-session -- sam deploy

deploy-site:
	aws-vault exec mnguyen --no-session -- aws s3 sync ./resume s3://mnguyen-bucket

invoke-get: 
	sam build && aws-vault exec mnguyen --no-session -- sam local invoke GetFunction 
invoke-put:
	sam build && aws-vault exec mnguyen --no-session -- sam local invoke PutFunction 