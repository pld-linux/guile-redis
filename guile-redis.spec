Summary:	Redis module for Guile
Summary(pl.UTF-8):	Moduł Redis dla języka Guile
Name:		guile-redis
Version:	2.2.0
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	https://download.savannah.gnu.org/releases/guile-redis/%{name}-%{version}.tar.gz
# Source0-md5:	00802cf1a8e6e226655ff714011b67a4
URL:		https://github.com/aconchillo/guile-redis
BuildRequires:	guile-devel >= 5:2.2
BuildRequires:	guile-devel < 5:3.2
BuildRequires:	pkgconfig
Requires:	guile-libs >= 5:2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
guile-redis is a Guile module for the Redis (<https://redis.io/>)
key-value data store. It provides all commands up to Redis 7.0 and
supports multiple commands, pipelining and Pub/Sub.

%description -l pl.UTF-8
guile-redis to moduł Guile dla bazy danych klucz-wartość Redis
(<https://redis.io/>). Udostępnia wszystkie polecenia do Redis 7.0
włącznie i obsługuje wiele poleceń, potoki oraz Pub/Sub.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/guile/*.*/site-ccache/redis.go
%{_libdir}/guile/*.*/site-ccache/redis
%{_datadir}/guile/site/*.*/redis.scm
%{_datadir}/guile/site/*.*/redis
