Name:           kind
# renovate: datasource=github-releases depName=kubernetes-sigs/kind
Version:        0.11.0
Release:        1%{?dist}
Summary:        Kubernetes IN Docker - local clusters for testing Kubernetes

License:        ASL 2.0
URL:            https://kind.sigs.k8s.io
Source0:        https://kind.sigs.k8s.io/dl/v%{version}/kind-linux-amd64

%description
kind is a tool for running local Kubernetes clusters using Docker container “nodes”. 
kind was primarily designed for testing Kubernetes itself, but may be used for local development or CI.

%install
mkdir -p %{buildroot}/%{_bindir}
install -d %{buildroot}%{_bindir}
install -p -m 0755 %{_sourcedir}/kind-linux-amd64 %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu May 06 2021 Christian Köberl - 0.10.0-1
- Initial package.
