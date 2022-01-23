
/* Code to register embedded modules for meta path based loading if any. */

#include <Python.h>

#include "nuitka/constants_blob.h"

#include "nuitka/unfreezing.h"

/* Type bool */
#ifndef __cplusplus
#include "stdbool.h"
#endif

#if 0 > 0
static unsigned char *bytecode_data[0];
#else
static unsigned char **bytecode_data = NULL;
#endif

/* Table for lookup to find compiled or bytecode modules included in this
 * binary or module, or put along this binary as extension modules. We do
 * our own loading for each of these.
 */
extern PyObject *modulecode_discord(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_discord$bypass(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_discord$bypass$account(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_discord$bypass$gateway(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_discord$bypass$helpers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_discord$bypass$helpers$captcha(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_discord$bypass$helpers$email(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_discord$bypass$http(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_discord$bypass$remote_auth(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_discord$bypass$user(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_discord$context_properties(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_discord$enums(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_discord$errors(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_discord$recorder(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_discord$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);

static struct Nuitka_MetaPathBasedLoaderEntry meta_path_loader_entries[] = {
    {"discord", modulecode_discord, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"discord.bypass", modulecode_discord$bypass, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"discord.bypass.account", modulecode_discord$bypass$account, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"discord.bypass.gateway", modulecode_discord$bypass$gateway, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"discord.bypass.helpers", modulecode_discord$bypass$helpers, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"discord.bypass.helpers.captcha", modulecode_discord$bypass$helpers$captcha, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"discord.bypass.helpers.email", modulecode_discord$bypass$helpers$email, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"discord.bypass.http", modulecode_discord$bypass$http, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"discord.bypass.remote_auth", modulecode_discord$bypass$remote_auth, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"discord.bypass.user", modulecode_discord$bypass$user, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"discord.context_properties", modulecode_discord$context_properties, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"discord.enums", modulecode_discord$enums, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"discord.errors", modulecode_discord$errors, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"discord.recorder", modulecode_discord$recorder, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"discord.utils", modulecode_discord$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {NULL, NULL, 0, 0, 0}
};

static void _loadBytesCodesBlob()
{
    static bool init_done = false;

    if (init_done == false) {
        loadConstantsBlob((PyObject **)bytecode_data, ".bytecode");

        init_done = true;
    }
}


void setupMetaPathBasedLoader(void) {
    static bool init_done = false;
    if (init_done == false) {
        _loadBytesCodesBlob();
        registerMetaPathBasedUnfreezer(meta_path_loader_entries, bytecode_data);

        init_done = true;
    }


}

// This provides the frozen (compiled bytecode) files that are included if
// any.

// These modules should be loaded as bytecode. They may e.g. have to be loadable
// during "Py_Initialize" already, or for irrelevance, they are only included
// in this un-optimized form. These are not compiled by Nuitka, and therefore
// are not accelerated at all, merely bundled with the binary or module, so
// that CPython library can start out finding them.

struct frozen_desc {
    char const *name;
    int index;
    int size;
};

static struct frozen_desc _frozen_modules[] = {

    {NULL, 0, 0}
};


void copyFrozenModulesTo(struct _frozen *destination) {
    _loadBytesCodesBlob();

    struct frozen_desc *current = _frozen_modules;

    for (;;) {
        destination->name = (char *)current->name;
        destination->code = bytecode_data[current->index];
        destination->size = current->size;

        if (destination->name == NULL) break;

        current += 1;
        destination += 1;
    };
}

