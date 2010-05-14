# TODO
# - needs patched kernel
# - needs mountall upstart job
Summary:	Read files in advance during boot
Name:		ureadahead
Version:	0.100.0
Release:	0.1
License:	GPL v2+
Group:		Base
Source0:	http://launchpad.net/ureadahead/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	086d3f3584b7c54a0c8647c1fba6cec7
URL:		https://launchpad.net/ureadahead
BuildRequires:	e2fsprogs-devel >= 1.41
BuildRequires:	libblkid-devel >= 2.16
BuildRequires:	libnih-devel >= 1.0.0
BuildRequires:	pkgconfig
Requires:	upstart >= 0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
ureadahead (uber-readahead) is used during boot to read files in
advance of when they are needed such that they are already in the page
cache, improving boot performance.

%description -l en.UTF-8
ureadahead (über-readahead) is used during boot to read files in
advance of when they are needed such that they are already in the page
cache, improving boot performance.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/ureadahead/debugfs
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/init/ureadahead*.conf
%attr(755,root,root) %{_sbindir}/ureadahead
%{_mandir}/man8/ureadahead.8*
%dir /var/lib/ureadahead
%dir /var/lib/ureadahead/debugfs
