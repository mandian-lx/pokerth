Name: pokerth
Summary: PokerTH - play Texas Holdem Poker alone or online
Version: 0.8.3
Release: %mkrel 2
License: GPLv2+
Group: Games/Cards
URL: http://www.pokerth.net/
Source0: http://downloads.sourceforge.net/pokerth/PokerTH-%{version}-src.tar.bz2
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires: qt4-devel
BuildRequires: gnutls-devel
BuildRequires: boost-devel
BuildRequires: curl-devel
BuildRequires: SDL_mixer1.2-devel
BuildRequires: libgsasl-devel  
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
PokerTH is a multi-platform poker game.
It allows you to play the popular "Texas Hold'em" poker variant against up to 
six computer-opponents or play network games with people all over the world.

%package server
Summary: PokerTH server
Group: Games/Cards

%description server
PokerTH server.

%prep
%setup -q -n PokerTH-%{version}-src

%build
%qmake_qt4 pokerth.pro QMAKE_CXXFLAGS="%optflags -DBOOST_FILESYSTEM_VERSION=2"
%make

%install
%__rm -rf %{buildroot}
#data
%make INSTALL_ROOT=%{buildroot} install
#binaries
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/
install -m 755 bin/%{name}_server %{buildroot}%{_bindir}/
#man page
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 docs/%{name}.1 %{buildroot}%{_mandir}/man1/
#icon
install -d -m 755 %{buildroot}%{_iconsdir}
install -m 644 %{name}.png %{buildroot}%{_iconsdir}/%{name}.png
#menu
install -d -m 755 %{buildroot}%{_datadir}/applications/
install -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/

%if %mdkversion < 200900
%post
%{update_desktop_database}
%{update_menus}
%endif
 
%if %mdkversion < 200900
%postun
%{clean_desktop_database}
%{clean_menus} 
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ChangeLog docs/net_protocol.txt
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png

%files server
%defattr(0644,root,root,0755)
%doc ChangeLog COPYING docs/net_protocol.txt
%attr(0755,root,root) %{_bindir}/%{name}_server
