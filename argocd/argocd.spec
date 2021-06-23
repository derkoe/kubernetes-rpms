Name:           argocd
# renovate: datasource=github-releases depName=argoproj/argo-cd
Version:        2.0.4
Release:        1%{?dist}
Summary:        Declarative GitOps CD for Kubernetes

Group:          Applications/System
License:        ASL 2.0
URL:            https://argoproj.github.io/
Source0:        https://github.com/argoproj/argo-cd/releases/download/v%{version}/argocd-linux-amd64

%description
%{summary}.

%prep
# nothing to do

%build
chmod +x %{_sourcedir}/argocd-linux-amd64

%install
mkdir -p %{buildroot}%{_bindir}
cp %{_sourcedir}/argocd-linux-amd64 %{buildroot}%{_bindir}/argocd

%clean
rm -rf %{buildroot}

%files
%{_bindir}/argocd
