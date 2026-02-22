Summary:	Swedish dictionary for aspell
Summary(pl.UTF-8):	Słownik szwedzki dla aspella
Name:		aspell-sv
Version:	0.51
%define	subv	0
Release:	3
Epoch:		1
License:	GPL
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/sv/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	d180c781f8986ea0f65b6b18f02a494e
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Swedish dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik szwedzki (lista słów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_prefix}/lib/aspell/*
%{_datadir}/aspell/*
