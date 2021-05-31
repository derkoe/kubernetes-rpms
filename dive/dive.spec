Name:           dive
# renovate: datasource=github-releases depName=wagoodman/dive
Version:        0.10.0
Release:        1%{?dist}
Summary:        A tool for exploring each layer in a docker image

License:        MIT
URL:            https://github.com/wagoodman/dive
Source0:        https://github.com/wagoodman/dive/releases/download/v%{version}/dive_%{version}_linux_amd64.tar.gz

%description
A tool for exploring a docker image, layer contents, and discovering ways to shrink the size of your Docker/OCI image.

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/licenses/%{name}
mkdir -p %{buildroot}/%{_docdir}/%{name}

tar xzf %{_sourcedir}/dive_%{version}_linux_amd64.tar.gz
install -p -m 755 dive %{buildroot}/%{_bindir}
install -p -m 644 LICENSE %{buildroot}/%{_datadir}/licenses/%{name}/
install -p -m 644 README.md %{buildroot}/%{_docdir}/%{name}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
