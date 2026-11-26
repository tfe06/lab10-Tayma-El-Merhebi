"""Copy the application to a local directory outside the Jenkins workspace."""

import os
from pathlib import Path
import shutil


def deploy():
    default_target = (
        Path(__file__).resolve().parent.parent
        / "jenkins_deployments" / "Python-CI-CD"
    )
    target = Path(os.environ.get("DEPLOY_DIR", str(default_target)))
    target.mkdir(parents=True, exist_ok=True)
    shutil.copy2(Path(__file__).with_name("app.py"), target / "app.py")
    print(f"Application deployed to {target / 'app.py'}")


if __name__ == "__main__":
    deploy()
