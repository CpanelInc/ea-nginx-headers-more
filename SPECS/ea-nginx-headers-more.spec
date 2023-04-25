Name:           ea-nginx-headers-more
Version:        0.34
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 1
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        This module allows you to add, set, or clear any output or input header that you specify.
License:        Custom, see LICENSE file.
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
Vendor:         cPanel, Inc.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires:       ea-nginx

Source0:        v%{version}.tar.gz
Source1:        ea-nginx-headers-more-module.conf

%description
This module allows you to add, set, or clear any output or input header that you specify. This is
an enhanced version of the standard headers module because it provides more utilities like resetting
or clearing "builtin headers" like Content-Type, Content-Length, and Server. It also allows you to
specify an optional HTTP status code criteria using the -s option and an optional content type criteria using
the -t option while modifying the output headers with the more_set_headers and more_clear_headers directives

%prep
%setup -q -n headers-more-nginx-module-%{version}

%build
echo "TODO: build dynamic module using ea-nginx w/ --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx etc"

%install
set -x 

install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/nginx/conf.d/modules/ea-nginx-headers-more-module.conf

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
/etc/nginx/conf.d/modules/ea-nginx-echo-module.conf

%changelog
* Mon Apr 24 2023 Brian Mendoza <brian.mendoza@cpanel.net> - 0.34-1
- ZC-10474: Create ea-nginx-headers-more module