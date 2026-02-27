#!/usr/bin/node
if (process.argv[2] && Number(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    const size = process.argv[2];
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
