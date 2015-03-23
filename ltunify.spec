Summary:	Logitech Unifying for Linux
Name:		ltunify
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications/System
# git clone https://git.lekensteyn.nl/ltunify.git
Source0:	%{name}-%{version}.tar.xz
# Source0-md5:	7f13f1f3b9603f58629e16cfe91bf485
URL:		https://lekensteyn.nl/logitech-unifying.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pair, unpair or list information about wireless devices like keyboards
and mice that use the Logitech(r) Unifying receiver.

%description -l en_US.utf8
Pair, unpair or list information about wireless devices like keyboards
and mice that use the Logitech® Unifying receiver.

%prep
%setup -q

%build
%{__make} \
	PACKAGE_VERSION=%{version} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	udevrulesdir=/lib/udev/rules.d \
	bindir=%{_bindir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.txt keyboard.txt notes.txt registers.txt
%attr(755,root,root) %{_bindir}/%{name}
/lib/udev/rules.d/42-logitech-unify-permissions.rules
