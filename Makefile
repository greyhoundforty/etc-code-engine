push:
	git add . && git commit -m "update" && git push

gh-run-list:
	gh run list --workflow="ICR Image build and push" --limit 1

gh-run-watch:
	gh run watch && echo "run is done!"

# Submit new job run to Code Engine
ce-submit-job:
	ibmcloud ce jobrun submit --name $$(date +%Y%m%d%H%M%S)-run  --job python-get-env -o json | jq -r '.metadata.name' > jobrun_id.txt

