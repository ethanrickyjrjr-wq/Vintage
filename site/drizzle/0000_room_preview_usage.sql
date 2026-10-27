CREATE TABLE `room_preview_usage` (
  `day` text NOT NULL,
  `visitor` text NOT NULL,
  `uses` integer DEFAULT 0 NOT NULL,
  PRIMARY KEY (`day`, `visitor`)
);
