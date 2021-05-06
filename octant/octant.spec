Name:           octant
Version:        0.19.0
Release:        1%{?dist}
Summary:        A highly extensible platform for developers to better understand the complexity of Kubernetes clusters.

License:        Apache-2.0
URL:            https://kind.sigs.k8s.io
Source0:        https://github.com/vmware-tanzu/octant/releases/download/v%{version}/octant_%{version}_Linux-64bit.tar.gz

%description
Octant is a tool for developers to understand how applications run on a Kubernetes cluster. 
It aims to be part of the developer's toolkit for gaining insight and approaching complexity 
found in Kubernetes. Octant offers a combination of introspective tooling, cluster navigation, 
and object management along with a plugin system to further extend its capabilities.

%install
mkdir -p %{buildroot}/%{_bindir}

tar xzf %{_sourcedir}/octant_%{version}_Linux-64bit.tar.gz
install -p -m 0755 octant_%{version}_Linux-64bit/octant %{buildroot}/%{_bindir}

%files
%{_bindir}/%{name}

%changelog
* Thu May 06 2021 Christian Köberl - 0.19.0-1
- Initial package.
