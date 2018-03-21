#include <db/db.hpp>

#include <connector/connector.hpp>

#include <iostream>

namespace db {
void request() {
  connector::connect();
  std::cout << "request has been made" << std::endl;
}
}  // namespace db
