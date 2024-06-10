/* eslint-disable no-plusplus */
export default function PascalTriangle(PasLen = 0) {
  const baseList = [[1], [1, 1]];

  if (PasLen === 0 || PasLen === 1) {
    return ([[1]]);
  } if (PasLen === 2) {
    return ((baseList));
  }

  for (let pI = 1; pI < (PasLen - 1); pI++) {
    const pList = [1];
    for (let pIi = 0, pIj = 1; pIj < (baseList[pI]).length; pIi++, pIj++) {
      pList.push(baseList[pI][pIi] + baseList[pI][pIj]);
    }
    pList.push(1);
    baseList.push(pList);
  }
  return baseList;
}
