#pragma once

#ifdef WIN32
#define CONNECTOR_EXPORT __declspec(dllexport)
#else
#define CONNECTOR_EXPORT
#endif

namespace connector {
CONNECTOR_EXPORT void connect();
}
