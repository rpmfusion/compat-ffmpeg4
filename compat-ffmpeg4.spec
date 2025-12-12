%undefine _package_note_file
%global __provides_exclude_from ^(%{_libdir}/pkgconfig)/.*$
%global __requires_exclude_from ^(%{_libdir}/pkgconfig)/.*$

# Cuda and others are only available on some arches
%if 0%{?el7}
%global _without_aom      1
%global _without_dav1d    1
%global _without_frei0r   1
%global _without_opus     1
%global _without_vpx      1
%endif

%if 0%{?el9}
%global _without_frei0r   1
%global _without_jack     1
%ifarch x86_64
%global _with_mfx         1
%endif
%endif

%if 0%{?fedora}
%ifarch x86_64
%global _with_mfx         1
%endif
%endif

# Disable nvenc when not relevant
%ifnarch x86_64 aarch64
%global _without_nvenc    1
%endif

%if 0%{?_without_gpl}
%global lesser L
%endif

%if 0%{!?_without_amr} || 0%{?_with_gmp}
%global ffmpeg_license %{?lesser}GPLv3+
%else
%global ffmpeg_license %{?lesser}GPLv2+
%endif

Summary:        Digital VCR and streaming server
Name:           compat-ffmpeg4
Version:        4.4.6
Release:        2%{?dist}
License:        %{ffmpeg_license}
URL:            https://ffmpeg.org/
Source0:        %{url}/releases/ffmpeg-%{version}.tar.xz
Source1:        %{url}/releases/ffmpeg-%{version}.tar.xz.asc
Source2:        %{url}/ffmpeg-devel.asc
Patch0:         configure-fix-nvenc-detection.patch
Patch1:         nvenc-stop-using-deprecated-rc-modes.patch
Patch2:         nvenc-support-SDK-12.2-bit-depth-API.patch
Patch3:         avcodec-x86-pngdsp-add-missing-emms-at-the-end-of-ad.patch
Patch4:         qsv-remove-mfx-prefix-from-mfx-headers.patch
Patch5:         avfilter-compress-CUDA-PTX-code-if-possible.patch
Patch6:         configure-rename-POSIX-ioctl-check.patch

BuildRequires:  gcc
BuildRequires:  alsa-lib-devel
BuildRequires:  AMF-devel
BuildRequires:  bzip2-devel
%{?_with_faac:BuildRequires: faac-devel}
%{?_with_fdk_aac:BuildRequires: fdk-aac-devel}
%{?_with_flite:BuildRequires: flite-devel}
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  fribidi-devel
%{!?_without_frei0r:BuildRequires: frei0r-devel}
%{?_with_gme:BuildRequires: game-music-emu-devel}
BuildRequires:  gnupg2
BuildRequires:  gnutls-devel
BuildRequires:  gsm-devel
%{?_with_ilbc:BuildRequires: ilbc-devel}
BuildRequires:  lame-devel >= 3.98.3
%{!?_without_jack:BuildRequires: jack-audio-connection-kit-devel}
%{!?_without_ladspa:BuildRequires: ladspa-devel}
%{!?_without_aom:BuildRequires:  libaom-devel}
%{!?_without_dav1d:BuildRequires:  libdav1d-devel >= 0.2.1}
%{!?_without_ass:BuildRequires:  libass-devel}
%{!?_without_bluray:BuildRequires:  libbluray-devel}
%{?_with_bs2b:BuildRequires: libbs2b-devel}
%{?_with_caca:BuildRequires: libcaca-devel}
%{!?_without_cdio:BuildRequires: libcdio-paranoia-devel}
%{?_with_chromaprint:BuildRequires: libchromaprint-devel}
%{?_with_crystalhd:BuildRequires: libcrystalhd-devel}
%if 0%{?_with_ieee1394}
BuildRequires:  libavc1394-devel
BuildRequires:  libdc1394-devel
BuildRequires:  libiec61883-devel
%endif
BuildRequires:  libdrm-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libGL-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmysofa-devel
BuildRequires:  libopenmpt-devel
BuildRequires:  librsvg2-devel
%{?_with_rtmp:BuildRequires: librtmp-devel}
BuildRequires:  libssh-devel
BuildRequires:  libtheora-devel
BuildRequires:  libv4l-devel
%{?!_without_vaapi:BuildRequires: libva-devel >= 0.31.0}
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
%{?!_without_vpx:BuildRequires: libvpx-devel >= 1.4.0}
%{?_with_mfx:BuildRequires: pkgconfig(libmfx) >= 1.23-1}
%ifarch %{ix86} x86_64
BuildRequires:  nasm
%endif
%{?_with_webp:BuildRequires: libwebp-devel}
%{?_with_netcdf:BuildRequires: netcdf-devel}
%{?_with_rpi:BuildRequires: raspberrypi-vc-devel}
%{!?_without_nvenc:BuildRequires: nv-codec-headers}
%{!?_without_amr:BuildRequires: opencore-amr-devel vo-amrwbenc-devel}
%{?_with_omx:BuildRequires: libomxil-bellagio-devel}
BuildRequires:  libxcb-devel
BuildRequires:  libxml2-devel
%{!?_without_openal:BuildRequires: openal-soft-devel}
%if 0%{!?_without_opencl:1}
%if 0%{?fedora}
BuildRequires:  opencl-headers OpenCL-ICD-Loader-devel
%else
BuildRequires:  opencl-headers pkgconfig(OpenCL)
%endif
%endif
%{?_with_opencv:BuildRequires: opencv-devel}
BuildRequires:  openjpeg2-devel
%{!?_without_opus:BuildRequires: opus-devel >= 1.1.3}
%{!?_without_pulse:BuildRequires: pulseaudio-libs-devel}
BuildRequires:  perl(Pod::Man)
%{?_with_rubberband:BuildRequires: rubberband-devel}
%{?_with_snappy:BuildRequires: snappy-devel}
BuildRequires:  soxr-devel
BuildRequires:  speex-devel
BuildRequires:  pkgconfig(srt)
%{?_with_tesseract:BuildRequires: tesseract-devel}
#BuildRequires:  texi2html
BuildRequires:  texinfo
%{?_with_twolame:BuildRequires: twolame-devel}
%{?_with_wavpack:BuildRequires: wavpack-devel}
%{!?_without_vidstab:BuildRequires:  vid.stab-devel}
%{!?_without_x264:BuildRequires: x264-devel >= 0.0.0-0.31}
%{!?_without_x265:BuildRequires: x265-devel}
%{!?_without_xvid:BuildRequires: xvidcore-devel}
%{!?_without_zimg:BuildRequires:  zimg-devel >= 2.7.0}
BuildRequires:  zlib-devel
%{?_with_zmq:BuildRequires: zeromq-devel}
%{!?_without_zvbi:BuildRequires: zvbi-devel}

%description
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.

!!! BIG FAT WARNING!!!
This package is made for compatibility with older components
It is not intended to be used in insecure environment.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       pkgconfig
Conflicts:      ffmpeg-devel
Conflicts:      ffmpeg-free-devel

%description    devel
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains development files for %{name}

# Don't use the %%configure macro as this is not an autotool script
%global ff_configure \
./configure \\\
    --prefix=%{_prefix} \\\
    --bindir=%{_bindir} \\\
    --datadir=%{_datadir}/%{name} \\\
    --docdir=%{_docdir}/%{name} \\\
    --incdir=%{_includedir}/%{name} \\\
    --libdir=%{_libdir} \\\
    --mandir=%{_mandir} \\\
    --arch=%{_target_cpu} \\\
    --optflags="%{optflags} -Wno-int-conversion" \\\
    --extra-ldflags="%{?__global_ldflags}" \\\
    --disable-manpages \\\
    %{!?_without_amr:--enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libvo-amrwbenc --enable-version3} \\\
    --enable-bzlib \\\
    %{?_with_chromaprint:--enable-chromaprint} \\\
    %{!?_with_crystalhd:--disable-crystalhd} \\\
    --enable-fontconfig \\\
    %{!?_without_frei0r:--enable-frei0r} \\\
    --enable-gcrypt \\\
    %{?_with_gmp:--enable-gmp --enable-version3} \\\
    --enable-gnutls \\\
    %{!?_without_ladspa:--enable-ladspa} \\\
    %{!?_without_aom:--enable-libaom} \\\
    %{!?_without_dav1d:--enable-libdav1d} \\\
    %{!?_without_ass:--enable-libass} \\\
    %{!?_without_bluray:--enable-libbluray} \\\
    %{?_with_bs2b:--enable-libbs2b} \\\
    %{?_with_caca:--enable-libcaca} \\\
    %{?_with_cuvid:--enable-cuvid --enable-nonfree} \\\
    %{!?_without_cdio:--enable-libcdio} \\\
    %{?_with_ieee1394:--enable-libdc1394 --enable-libiec61883} \\\
    --enable-libdrm \\\
    %{?_with_faac:--enable-libfaac --enable-nonfree} \\\
    %{?_with_fdk_aac:--enable-libfdk-aac --enable-nonfree} \\\
    %{?_with_flite:--enable-libflite} \\\
    %{!?_without_jack:--enable-libjack} \\\
    --enable-libfreetype \\\
    %{!?_without_fribidi:--enable-libfribidi} \\\
    %{?_with_gme:--enable-libgme} \\\
    --enable-libgsm \\\
    %{?_with_ilbc:--enable-libilbc} \\\
    %{?_with_libnpp:--enable-libnpp --enable-nonfree} \\\
    --enable-libmp3lame \\\
    --enable-libmysofa \\\
    %{?_with_netcdf:--enable-netcdf} \\\
    %{?_with_mmal:--enable-mmal} \\\
    %{!?_without_nvenc:--enable-nvenc} \\\
    %{?_with_omx:--enable-omx} \\\
    %{?_with_omx_rpi:--enable-omx-rpi} \\\
    %{!?_without_openal:--enable-openal} \\\
    %{!?_without_opencl:--enable-opencl} \\\
    %{?_with_opencv:--enable-libopencv} \\\
    %{!?_without_opengl:--enable-opengl} \\\
    --enable-libopenjpeg \\\
    --enable-libopenmpt \\\
    %{!?_without_opus:--enable-libopus} \\\
    %{!?_without_pulse:--enable-libpulse} \\\
    --enable-librsvg \\\
    %{?_with_rtmp:--enable-librtmp} \\\
    %{?_with_rubberband:--enable-librubberband} \\\
    %{?_with_snappy:--enable-libsnappy} \\\
    --enable-libsoxr \\\
    --enable-libspeex \\\
    --enable-libssh \\\
    %{?_with_tesseract:--enable-libtesseract} \\\
    --enable-libtheora \\\
    %{?_with_twolame:--enable-libtwolame} \\\
    --enable-libvorbis \\\
    --enable-libv4l2 \\\
    %{!?_without_vidstab:--enable-libvidstab} \\\
    %{!?_without_vpx:--enable-libvpx} \\\
    %{?_with_webp:--enable-libwebp} \\\
    %{!?_without_x264:--enable-libx264} \\\
    %{!?_without_x265:--enable-libx265} \\\
    %{!?_without_xvid:--enable-libxvid} \\\
    --enable-libxml2 \\\
    %{!?_without_zimg--enable-libzimg} \\\
    %{?_with_zmq:--enable-libzmq} \\\
    %{!?_without_zvbi:--enable-libzvbi} \\\
    --enable-avfilter \\\
    --enable-libmodplug \\\
    --enable-postproc \\\
    --enable-pthreads \\\
    --disable-static \\\
    --enable-shared \\\
    %{!?_without_gpl:--enable-gpl} \\\
    --disable-debug \\\
    --disable-stripping


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n ffmpeg-%{version}

# fix -O3 -g in host_cflags
sed -i "s|check_host_cflags -O3|check_host_cflags %{optflags}|" configure

%build
%{ff_configure}\
    --shlibdir=%{_libdir} \
    --disable-doc \
    --disable-ffmpeg --disable-ffplay --disable-ffprobe \
%ifnarch %{ix86}
    --enable-lto \
%endif
%ifarch %{ix86}
    --cpu=%{_target_cpu} \
%endif
    %{?_with_mfx:--enable-libmfx} \
%ifarch %{ix86} x86_64 %{power64}
    --enable-runtime-cpudetect \
%endif
%ifarch %{power64}
%ifarch ppc64
    --cpu=g5 \
%endif
%ifarch ppc64p7
    --cpu=power7 \
%endif
%ifarch ppc64le
    --cpu=power8 \
%endif
    --enable-pic \
%endif
%ifarch %{arm}
    --disable-runtime-cpudetect --arch=arm \
%ifarch armv6hl
    --cpu=armv6 \
%endif
%ifarch armv7hl armv7hnl
    --cpu=armv7-a \
    --enable-vfpv3 \
    --enable-thumb \
%endif
%ifarch armv7hl
    --disable-neon \
%endif
%ifarch armv7hnl
    --enable-neon \
%endif
%endif
    || cat ffbuild/config.log

%make_build V=1

%install
%make_install V=1
rm -rf %{buildroot}/%{_datadir}/compat-ffmpeg4/

%ldconfig_scriptlets


%files
%doc CREDITS README.md
%license COPYING.*
%{_libdir}/lib*.so.*


%files devel
%doc MAINTAINERS doc/APIchanges doc/*.txt
%{_includedir}/%{name}
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/lib*.so


%changelog
* Fri Dec 12 2025 Nicolas Chauvet <kwizart@gmail.com> - 4.4.6-2
- Rebuilt for libbluray

* Tue Sep 16 2025 Nicolas Chauvet <kwizart@gmail.com> - 4.4.6-1
- Update to 4.4.6

* Thu Sep 04 2025 Sérgio Basto <sergio@serjux.com> - 4.4.5-5
- Rebuild for x264

* Sun Jul 27 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 23 2024 Leigh Scott <leigh123linux@gmail.com> - 4.4.5-2
- Rebuild for new x265

* Sun Aug 04 2024 Leigh Scott <leigh123linux@gmail.com> - 4.4.5-1
- Update to 4.4.5

* Thu Aug 01 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 06 2024 Leigh Scott <leigh123linux@gmail.com> - 4.4.4-5
- Rebuild for new x265 version

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Leigh Scott <leigh123linux@gmail.com> - 4.4.4-3
- rebuilt

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 13 2023 Leigh Scott <leigh123linux@gmail.com> - 4.4.4-1
- Update to 4.4.4

* Wed Mar 22 2023 Nicolas Chauvet <kwizart@gmail.com> - 4.4.3-3
- rebuilt

* Wed Nov 16 2022 Nicolas Chauvet <kwizart@gmail.com> - 4.4.3-2
- Rebuilt

* Mon Oct 10 2022 Leigh Scott <leigh123linux@gmail.com> - 4.4.3-1
- Update to 4.4.3

* Sun Sep 04 2022 Leigh Scott <leigh123linux@gmail.com> - 4.4.2-6
- Remove pkgconfig provides from devel

* Sun Sep 04 2022 Leigh Scott <leigh123linux@gmail.com> - 4.4.2-5
- Use standard location for pkgconfig and development libs

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Jun 23 2022 Robert-André Mauchin <zebob.m@gmail.com> - 4.4.2-3
- Rebuilt for new AOM, dav1d, rav1e and svt-av1

* Sun Jun 12 2022 Sérgio Basto <sergio@serjux.com> - 4.4.2-2
- Mass rebuild for x264-0.164

* Fri Apr 15 2022 Leigh Scott <leigh123linux@gmail.com> - 4.4.2-1
- Update to 4.4.2

* Mon Feb 14 2022 Leigh Scott <leigh123linux@gmail.com> - 4.4.1-1
- Update to 4.4.1

* Wed Feb 09 2022 Leigh Scott <leigh123linux@gmail.com> - 4.3.3-1
- Initial build


