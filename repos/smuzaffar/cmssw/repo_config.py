from cms_static import GH_CMSSW_ORGANIZATION,GH_CMSSW_REPO,CMSBUILD_GH_USER
from os.path import basename,dirname,abspath
GH_TOKEN="~/.github-token-cmsbot-write"
GH_TOKEN_READONLY="~/.github-token-readonly"
CONFIG_DIR=dirname(abspath(__file__))
CMSBUILD_USER="cmsbot"
GH_REPO_ORGANIZATION=basename(dirname(CONFIG_DIR))
CREAT_EXTERNAL_ISSUE=False
JENKINS_SERVER="http://cmsjenkins05.cern.ch:8080/jenkins"
IGNORE_ISSUES = [10]
def file2Package(filename): return GH_REPO_ORGANIZATION
