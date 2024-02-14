Name:           ea-nginx-headers-more
Version:        0.34
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 5
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        This module allows you to add, set, or clear any output or input header that you specify.
License:        BSD
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
Vendor:         cPanel, Inc.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  ea-nginx-ngxdev
Requires:       ea-nginx

Source0:        v%{version}.tar.gz
Source1:        ea-nginx-headers-more-filter-module.conf

%description
This module allows you to add, set, or clear any output or input header that you specify. This is
an enhanced version of the standard headers module because it provides more utilities like resetting
or clearing "builtin headers" like Content-Type, Content-Length, and Server. It also allows you to
specify an optional HTTP status code criteria using the -s option and an optional content type criteria using
the -t option while modifying the output headers with the more_set_headers and more_clear_headers directives

%prep
%setup -q -n headers-more-nginx-module-%{version}

%build
set -x

mypwd=`pwd`
# You will be in ./nginx-build after this source()
#    so that configure and make etc can happen.
# We probably want to popd back when we are done in there
. /opt/cpanel/ea-nginx-ngxdev/set_NGINX_CONFIGURE_array.sh
./configure "${NGINX_CONFIGURE[@]}" --add-dynamic-module=$mypwd

make
popd

%install
set -x 

install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/nginx/conf.d/modules/ea-nginx-headers-more-filter-module.conf
install -D ./nginx-build/objs/ngx_http_headers_more_filter_module.so $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ngx_http_headers_more_filter_module.so

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
/etc/nginx/conf.d/modules/ea-nginx-headers-more-filter-module.conf
%attr(0755,root,root) %{_libdir}/nginx/modules/ngx_http_headers_more_filter_module.so

%changelog
* Wed Feb 14 2024 Cory McIntire <cory@cpanel.net> - 0.34-5
- EA-11973: Build against ea-nginx version v1.25.4

* Thu Oct 26 2023 Cory McIntire <cory@cpanel.net> - 0.34-4
- EA-11772: Build against ea-nginx version v1.25.3

* Thu Aug 24 2023 Cory McIntire <cory@cpanel.net> - 0.34-3
- EA-11631: Build against ea-nginx version v1.25.2

* Thu Jun 15 2023 Cory McIntire <cory@cpanel.net> - 0.34-2
- EA-11496: Build against ea-nginx version v1.25.1

* Mon Apr 24 2023 Brian Mendoza <brian.mendoza@cpanel.net> - 0.34-1
- ZC-10474: Create ea-nginx-headers-more module