#
# This file is in the Public Domain.
#

PROJ=		nv

CFLAGS+=	-std=c99 -O2 -g -Wall -Wextra -Werror
CFLAGS+=	-D_POSIX_C_SOURCE=200809L
CFLAGS+=	-D_GNU_SOURCE -D_DEFAULT_SOURCE
CFLAGS+=	-D__FBSDID\(x\)=

#
# Extended warning flags.
#
#CFLAGS+=	-Wno-unknown-warning-option # gcc vs clang

CFLAGS+=	-Wstrict-prototypes -Wmissing-prototypes -Wpointer-arith
CFLAGS+=	-Wmissing-declarations -Wredundant-decls -Wnested-externs
CFLAGS+=	-Wshadow -Wcast-qual -Wcast-align -Wwrite-strings
CFLAGS+=	-Wold-style-definition
#CFLAGS+=	-Wsuggest-attribute=noreturn -Wjump-misses-init

# New GCC 6/7 flags:
#CFLAGS+=	-Wduplicated-cond -Wmisleading-indentation -Wnull-dereference
#CFLAGS+=	-Wduplicated-branches -Wrestrict

ifeq ($(MAKECMDGOALS),tests)
DEBUG=		1
endif

ifeq ($(DEBUG),1)
CFLAGS+=	-Og -DDEBUG -fno-omit-frame-pointer
else
CFLAGS+=	-DNDEBUG
endif

LIB=		lib$(PROJ)
INCS=		nv.h dnv.h
OBJS=		nvlist.o nvpair.o dnvlist.o # msgio.o

MANS=		nv.3

TEST_FILES:=	$(filter-out tests/nvlist_send_recv_test.c,$(wildcard tests/*.c))
TESTS:=		$(patsubst tests/%.c,%,$(TEST_FILES))

$(LIB).la:	LDFLAGS+=	-rpath $(LIBDIR) -version-info 1:0:0
install/%.la:	ILIBDIR=	$(DESTDIR)/$(LIBDIR)
install:	IINCDIR=	$(DESTDIR)/$(INCDIR)/
install:	IMANDIR=	$(DESTDIR)/$(MANDIR)/man3/

obj: $(OBJS)

lib: $(LIB).la

%.lo: %.c
	libtool --mode=compile --tag CC $(CC) $(CFLAGS) -c $<

$(LIB).la: $(shell echo $(OBJS) | sed 's/\.o/\.lo/g')
	libtool --mode=link --tag CC $(CC) $(LDFLAGS) -o $@ $(notdir $^)

install/%.la: %.la
	mkdir -p $(ILIBDIR)
	libtool --mode=install install -c $(notdir $@) $(ILIBDIR)/$(notdir $@)

install: $(addprefix install/,$(LIB).la)
	libtool --mode=finish $(LIBDIR)
	mkdir -p $(IINCDIR) && install -c $(INCS) $(IINCDIR)
	mkdir -p $(IMANDIR) && install -c $(MANS) $(IMANDIR)

%_test: $(OBJS)
	$(CC) $(CFLAGS) -I. $^ tests/$@.c -o $@ $(LDFLAGS)

tests: $(TESTS)
	@ for T in $(TESTS); do echo ./$$T; ./$$T; done | \
	    awk '1; /not ok/ { exit 1; }'

clean:
	libtool --mode=clean rm
	@ rm -rf .libs *.o *.lo *.la $(TESTS)

.PHONY: all obj lib tests install clean
