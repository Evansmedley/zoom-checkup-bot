gcloud iam workload-identity-pools create github-actions-pool \
--location="global" \
--description="The pool to authenticate GitHub actions." \
--display-name="GitHub Actions Pool"

gcloud iam workload-identity-pools providers create-oidc github-actions-oidc \
--workload-identity-pool="github-actions-pool" \
--issuer-uri="https://token.actions.GitHubusercontent.com/" \
--attribute-mapping="google.subject=assertion.sub,attribute.repository=assertion.repository,attribute.repository_owner=assertion.repository_owner,attribute.branch=assertion.sub.extract('/heads/{branch}/')" \
--location=global \
--attribute-condition="assertion.repository_owner=='Evansmedley'"

gcloud iam service-accounts create checkup-bot-sa --display-name="Checkup Bot Service Account" --description="manages the application resources"

gcloud iam service-accounts add-iam-policy-binding checkup-bot-sa@checkup-bot-406604.iam.gserviceaccount.com --role="roles/iam.workloadIdentityUser" --member="principal://iam.googleapis.com/projects/358322538977/locations/global/workloadIdentityPools/github-actions-pool/subject/repo:Evansmedley/zoom-checkup-bot:ref:refs/heads/main"
