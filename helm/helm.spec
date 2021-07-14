Name:           helm
# renovate: datasource=github-releases depName=helm/helm
Version:        3.6.3
Release:        1%{?dist}
Summary:        The Kubernetes Package Manager

License:        ASL 2.0
URL:            https://github.com/helm/helm
Source0:        https://get.helm.sh/helm-v%{version}-linux-amd64.tar.gz

%description
Helm helps you manage Kubernetes applications — Helm Charts help you define, install, and upgrade even the most complex Kubernetes application.

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/licenses/%{name}
mkdir -p %{buildroot}/%{_docdir}/%{name}

tar xzf %{_sourcedir}/helm-v%{version}-linux-amd64.tar.gz
install -p -m 755 linux-amd64/helm %{buildroot}/%{_bindir}
install -p -m 644 linux-amd64/LICENSE %{buildroot}/%{_datadir}/licenses/%{name}/
install -p -m 644 linux-amd64/README.md %{buildroot}/%{_docdir}/%{name}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
