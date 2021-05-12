Name:           helm
Version:        3.5.4
Release:        1%{?dist}
Summary:        The Kubernetes Package Manager

License:        ASL 2.0
URL:            https://github.com/helm/helm
Source0:        https://get.helm.sh/helm-v%{version}-linux-amd64.tar.gz

%description
Helm helps you manage Kubernetes applications — Helm Charts help you define, install, and upgrade even the most complex Kubernetes application.

%install
mkdir -p %{buildroot}/%{_bindir}

tar xzf %{_sourcedir}/helm-v%{version}-linux-amd64.tar.gz
install -p -m 755 linux-amd64/helm %{buildroot}/%{_bindir}
install -p -m 644 linux-amd64/LICENSE %{buildroot}/%{_datadir}/licenses/%{name}/
install -p -m 644 linux-amd64/README.md %{buildroot}/%{_docdir}/%{name}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
