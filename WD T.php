$oldUserId = $user->getId(); // create user then get ID [$this->oldUser->getId()]
Terminate.killAccount();

class Terminate {
	define("NukeLimit", 500);

	function getEditCount($oldUser) {
		$dbw = wfGetDB( DB_MASTER );
		$dbw->startAtomic( __METHOD__ );
		$editCount = $dbw->selectField(
				'user',
				'SUM(user_editcount)',
				[ 'user_id' => $oldUserId ],
				__METHOD__
			);

		$editCount = (int) $editCount; // cast to integer

		// wipe edit count of target users
		if ($editCount > 0) {
		$dbw->update( 'user',
					[ 'user_editcount' => 0 ],
					[ 'user_id' => $oldUserId ],
					__METHOD__
				);
		}
		$dbw->endAtomic( __METHOD__ );
	}

	function NukeIterations($editCount) {
		return $editCount % NukeLimit === 0 ? $editCount / NukeLimit : ceil($editCount / NukeLimit);
	}

	function killAccount($targets) {
		foreach($targets as $user) {
			$editCount = getEditCount($user);
			for ($i = 0; $i < $NukeIterations($editCount); $i++) {
				$user->Nuke::execute();
			}
		}
	}
}
